from datetime import datetime
from utility.load import load_expenses
from config import DATA_FILE


def filter_expenses():
    """Filter expenses by date range or category."""
    expenses = load_expenses(DATA_FILE)
    if not expenses:
        print("No expenses found.")
        return

    print("\n=== Filter Options ===")
    print("1. Filter by Date Range")
    print("2. Filter by Category")
    print("3. Filter by Both Date and Category")
    print("4. Back to Main Menu")
    
    choice = input("Choose filter option: ").strip()
    
    filtered_expenses = expenses.copy()
    
    if choice == "1":
        filtered_expenses = _filter_by_date(filtered_expenses)
    elif choice == "2":
        filtered_expenses = _filter_by_category(filtered_expenses)
    elif choice == "3":
        filtered_expenses = _filter_by_date(filtered_expenses)
        if filtered_expenses:
            filtered_expenses = _filter_by_category(filtered_expenses)
    elif choice == "4":
        return
    else:
        print("Invalid choice.")
        return
    
    if not filtered_expenses:
        print("No expenses found matching the criteria.")
        return
    
    _display_filtered_expenses(filtered_expenses)


def _filter_by_date(expenses):
    """Filter expenses by date range."""
    try:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        
        # Validate date formats
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        
        filtered = [
            exp for exp in expenses 
            if start_date <= exp["date"] <= end_date
        ]
        
        print(f"Found {len(filtered)} expenses between {start_date} and {end_date}")
        return filtered
        
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return []


def _filter_by_category(expenses):
    """Filter expenses by category."""
    # Show available categories
    categories = list(set(exp["category"] for exp in expenses))
    categories.sort()
    
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    try:
        choice = input("Enter category number or type category name: ").strip()
        
        # Check if it's a number (category selection)
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(categories):
                selected_category = categories[choice_num - 1]
            else:
                print("Invalid category number.")
                return []
        else:
            # Direct category name input
            selected_category = choice
        
        filtered = [
            exp for exp in expenses 
            if exp["category"].lower() == selected_category.lower()
        ]
        
        print(f"Found {len(filtered)} expenses in category '{selected_category}'")
        return filtered
        
    except ValueError:
        print("Invalid input.")
        return []


def _display_filtered_expenses(expenses):
    """Display filtered expenses in a formatted table."""
    print("\nFiltered Expenses:")
    print("ID | Date       | Amount | Category     | Note")
    print("-" * 55)
    
    for exp in expenses:
        print(f"{exp['id']:2d} | {exp['date']} | ₹{exp['amount']:>6.2f} | {exp['category']:<12} | {exp['note']}")
    
    print("-" * 55)
    total = sum(exp["amount"] for exp in expenses)
    print(f"Filtered Total: ₹{total:.2f}")
    
    # Category breakdown for filtered results
    if len(expenses) > 1:
        category_totals = {}
        for exp in expenses:
            category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
        
        print("\nCategory Breakdown:")
        for cat, amt in sorted(category_totals.items()):
            print(f" - {cat}: ₹{amt:.2f}")
    print()
