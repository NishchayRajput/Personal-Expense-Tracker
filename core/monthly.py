from datetime import datetime
from collections import defaultdict
from utility.load import load_expenses
from config import DATA_FILE


def monthly_summary():
    """Generate monthly summaries of expenses."""
    expenses = load_expenses(DATA_FILE)
    if not expenses:
        print("No expenses found.")
        return

    print("\n=== Monthly Summary Options ===")
    print("1. All Months Summary")
    print("2. Specific Month Summary")
    print("3. Year Comparison")
    print("4. Back to Main Menu")
    
    choice = input("Choose summary option: ").strip()
    
    if choice == "1":
        _show_all_months_summary(expenses)
    elif choice == "2":
        _show_specific_month_summary(expenses)
    elif choice == "3":
        _show_year_comparison(expenses)
    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def _show_all_months_summary(expenses):
    """Show summary for all months."""
    monthly_data = _group_by_month(expenses)
    
    if not monthly_data:
        print("No monthly data available.")
        return
    
    print("\n=== All Months Summary ===")
    print("Month       | Total Spent | Expenses | Avg/Expense")
    print("-" * 55)
    
    total_all_months = 0
    total_expenses_count = 0
    
    for month_key in sorted(monthly_data.keys()):
        month_expenses = monthly_data[month_key]
        total = sum(exp["amount"] for exp in month_expenses)
        count = len(month_expenses)
        avg = total / count if count > 0 else 0
        
        # Format month for display
        year, month = month_key.split('-')
        month_name = datetime(int(year), int(month), 1).strftime("%b %Y")
        
        print(f"{month_name:<11} | ₹{total:>9.2f} | {count:>8} | ₹{avg:>8.2f}")
        
        total_all_months += total
        total_expenses_count += count
    
    print("-" * 55)
    avg_all = total_all_months / total_expenses_count if total_expenses_count > 0 else 0
    print(f"{'TOTAL':<11} | ₹{total_all_months:>9.2f} | {total_expenses_count:>8} | ₹{avg_all:>8.2f}")
    
    # Show top spending month
    if monthly_data:
        top_month = max(monthly_data.keys(), 
                       key=lambda k: sum(exp["amount"] for exp in monthly_data[k]))
        top_amount = sum(exp["amount"] for exp in monthly_data[top_month])
        year, month = top_month.split('-')
        top_month_name = datetime(int(year), int(month), 1).strftime("%B %Y")
        
        print(f"\nHighest spending month: {top_month_name} (₹{top_amount:.2f})")


def _show_specific_month_summary(expenses):
    """Show detailed summary for a specific month."""
    try:
        year = input("Enter year (YYYY): ").strip()
        month = input("Enter month (1-12): ").strip()
        
        # Validate input
        year_int = int(year)
        month_int = int(month)
        if not (1 <= month_int <= 12):
            print("Month must be between 1 and 12.")
            return
        
        # Filter expenses for the specific month
        month_key = f"{year}-{month_int:02d}"
        month_expenses = [
            exp for exp in expenses 
            if exp["date"].startswith(month_key)
        ]
        
        if not month_expenses:
            month_name = datetime(year_int, month_int, 1).strftime("%B %Y")
            print(f"No expenses found for {month_name}.")
            return
        
        month_name = datetime(year_int, month_int, 1).strftime("%B %Y")
        print(f"\n=== {month_name} Detailed Summary ===")
        
        # Total and average
        total = sum(exp["amount"] for exp in month_expenses)
        count = len(month_expenses)
        avg_per_expense = total / count
        
        print(f"Total Spent: ₹{total:.2f}")
        print(f"Number of Expenses: {count}")
        print(f"Average per Expense: ₹{avg_per_expense:.2f}")
        
        # Category breakdown
        category_totals = defaultdict(float)
        for exp in month_expenses:
            category_totals[exp["category"]] += exp["amount"]
        
        print(f"\nCategory Breakdown:")
        for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amt / total) * 100
            print(f" - {cat:<15}: ₹{amt:>8.2f} ({percentage:>5.1f}%)")
        
        # Daily breakdown
        daily_totals = defaultdict(float)
        for exp in month_expenses:
            daily_totals[exp["date"]] += exp["amount"]
        
        print(f"\nDaily Spending:")
        for date in sorted(daily_totals.keys()):
            day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%a")
            print(f" - {date} ({day_name}): ₹{daily_totals[date]:.2f}")
        
        # Highest expense day
        highest_day = max(daily_totals.keys(), key=lambda k: daily_totals[k])
        highest_amount = daily_totals[highest_day]
        day_name = datetime.strptime(highest_day, "%Y-%m-%d").strftime("%A")
        print(f"\nHighest spending day: {highest_day} ({day_name}) - ₹{highest_amount:.2f}")
        
    except ValueError:
        print("Invalid year or month format.")


def _show_year_comparison(expenses):
    """Show year-over-year comparison."""
    yearly_data = defaultdict(lambda: defaultdict(list))
    
    # Group by year and month
    for exp in expenses:
        date_parts = exp["date"].split('-')
        year = date_parts[0]
        month = date_parts[1]
        yearly_data[year][month].append(exp)
    
    if len(yearly_data) < 2:
        print("Need at least 2 years of data for comparison.")
        return
    
    print("\n=== Year-over-Year Comparison ===")
    
    years = sorted(yearly_data.keys())
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # Header
    header = "Month    "
    for year in years:
        header += f"| {year}     "
    print(header)
    print("-" * len(header))
    
    # Monthly comparison
    for i, month in enumerate(months):
        row = f"{month_names[i]:<8} "
        for year in years:
            if month in yearly_data[year]:
                total = sum(exp["amount"] for exp in yearly_data[year][month])
                row += f"| ₹{total:>7.0f} "
            else:
                row += "|    -    "
        print(row)
    
    # Yearly totals
    print("-" * len(header))
    total_row = "TOTAL    "
    for year in years:
        year_total = sum(
            exp["amount"] for month_data in yearly_data[year].values() 
            for exp in month_data
        )
        total_row += f"| ₹{year_total:>7.0f} "
    print(total_row)
    
    # Growth analysis
    if len(years) >= 2:
        current_year = years[-1]
        previous_year = years[-2]
        
        current_total = sum(
            exp["amount"] for month_data in yearly_data[current_year].values() 
            for exp in month_data
        )
        previous_total = sum(
            exp["amount"] for month_data in yearly_data[previous_year].values() 
            for exp in month_data
        )
        
        if previous_total > 0:
            growth = ((current_total - previous_total) / previous_total) * 100
            trend = "UP" if growth > 0 else "DOWN" if growth < 0 else "->"
            print(f"\n{trend} YoY Growth ({previous_year} to {current_year}): {growth:+.1f}%")


def _group_by_month(expenses):
    """Group expenses by month (YYYY-MM)."""
    monthly_data = defaultdict(list)
    
    for exp in expenses:
        # Extract year-month from date (YYYY-MM-DD -> YYYY-MM)
        month_key = exp["date"][:7]
        monthly_data[month_key].append(exp)
    
    return dict(monthly_data)
