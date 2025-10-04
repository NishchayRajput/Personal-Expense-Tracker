# Personal Expense Tracker 

A simple yet powerful command-line expense tracking application built with Python. Keep track of your daily expenses, categorize them, and generate summary reports to better understand your spending habits.

## Features 

- **Add Expenses**: Record expenses with amount, date, description, and category
- **View Expenses**: Display all expenses in a formatted table with totals
- **Update Expenses**: Modify existing expense records
- **Delete Expenses**: Remove unwanted expense entries
- **Summary Reports**: Get spending insights by category and total amounts
- **Data Persistence**: All data is stored locally in JSON format
- **Date Validation**: Automatic date handling with manual override option
- **Category Management**: Organize expenses by custom categories
- **Filter Expenses**: Filter by date range, category, or both for targeted analysis
- **Monthly Summaries**: Comprehensive monthly reports with year-over-year comparisons

## Project Structure 

```
expense-tracker/
├── main.py                 # Main application entry point
├── config.py               # Configuration settings
├── expesnses.json          # Data storage file (auto-created)
├── README.md              # This file
├── core/                  # Core functionality modules
│   ├── add.py             # Add expense functionality
│   ├── view.py            # View expenses functionality
│   ├── update.py          # Update expense functionality
│   ├── delete.py          # Delete expense functionality
│   ├── summary.py         # Summary report functionality
│   ├── filter.py          # Expense filtering functionality
│   └── monthly.py         # Monthly summaries and analysis
└── utility/               # Utility functions
    ├── load.py            # Load data from JSON
    ├── save.py            # Save data to JSON
    └── generateId.py      # Generate unique IDs
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation & Setup

1. **Clone or download** the project to your local machine
2. **Navigate** to the project directory:
   ```bash
   cd evaao_assgnment
   ```
3. **Run** the application:
   ```bash
   python main.py
   ```

## How to Use

### Running the Application

```bash
python main.py
```

### Main Menu Options

When you run the application, you'll see a menu with the following options:

```
=== Personal Expense Tracker ===
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Summary Report
6. Filter Expenses
7. Monthly Summary
8. Exit
```

### 1. Adding an Expense

- Enter the amount (must be positive)
- Enter date in YYYY-MM-DD format (or leave blank for today's date)
- Add a description/note
- Specify a category (or leave blank for "General")

**Example:**
```
Enter amount: 250.50
Enter date (YYYY-MM-DD) or leave blank for today: 2025-10-04
Enter note/description: Lunch at restaurant
Enter category (optional): Food
```

### 2. Viewing Expenses

Displays all expenses in a formatted table showing:
- ID
- Date
- Amount
- Category
- Description
- Total spent

### 3. Updating an Expense

- View the list of expenses
- Enter the ID of the expense to update
- Modify any field (leave blank to keep current value)

### 4. Deleting an Expense

- View the list of expenses
- Enter the ID of the expense to delete
- Confirm deletion

### 5. Summary Report

Get insights including:
- Total amount spent
- Spending breakdown by category
- Category-wise totals

### 6. Filter Expenses 

Advanced filtering options to analyze specific subsets of your expenses:

**Filter Options:**
- **By Date Range**: Find expenses between specific dates
- **By Category**: View expenses from particular categories
- **Combined Filter**: Apply both date and category filters

**Features:**
- Interactive category selection (by number or name)
- Automatic category detection and listing
- Filtered totals and category breakdowns
- Clean, formatted display of results

**Example Usage:**
```
=== Filter Options ===
1. Filter by Date Range
2. Filter by Category
3. Filter by Both Date and Category

# Filter by date range
Enter start date (YYYY-MM-DD): 2025-10-01
Enter end date (YYYY-MM-DD): 2025-10-31

# Filter by category
Available categories:
1. Food
2. Transport
3. Entertainment
Enter category number or type category name: Food
```

### 7. Monthly Summary 

Comprehensive monthly analysis and reporting features:

**Summary Options:**

**a) All Months Summary**
- Overview of spending across all months
- Monthly totals, expense counts, and averages
- Identification of highest spending months
- Grand totals and overall statistics

**b) Specific Month Summary**
- Detailed breakdown for any chosen month
- Daily spending patterns
- Category analysis with percentages
- Highest spending day identification
- Average expense calculations

**c) Year-over-Year Comparison**
- Side-by-side comparison of multiple years
- Monthly breakdown across years
- Growth rate calculations
- Trend analysis with visual indicators

**Example Output:**
```
=== All Months Summary ===
Month       | Total Spent | Expenses | Avg/Expense
-------------------------------------------------------
Oct 2025    | ₹  2,500.00 |       15 | ₹  166.67
Nov 2025    | ₹  3,200.00 |       18 | ₹  177.78
-------------------------------------------------------
TOTAL       | ₹  5,700.00 |       33 | ₹  172.73

Highest spending month: November 2025 (₹3,200.00)
```

## Data Storage

- Expenses are stored in `expesnses.json` file
- Data persists between application runs
- JSON format ensures easy backup and portability
- File is automatically created on first use

## Configuration 

The application uses a `config.py` file for settings:

```python
DATA_FILE = "expesnses.json"
```

To change the data file location, simply modify the `DATA_FILE` variable in `config.py`.

## Sample Usage Session

```bash
## Sample Usage Session 

```bash
$ python main.py

=== Personal Expense Tracker ===
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Summary Report
6. Filter Expenses
7. Monthly Summary
8. Exit
Enter your choice: 1

Enter amount: 150.00
Enter date (YYYY-MM-DD) or leave blank for today: 
Enter note/description: Grocery shopping
Enter category (optional): Food
Expense added successfully!

Enter your choice: 6
=== Filter Options ===
1. Filter by Date Range
2. Filter by Category
3. Filter by Both Date and Category
4. Back to Main Menu
Choose filter option: 2

Available categories:
1. Food
2. General
Enter category number or type category name: 1
Found 1 expenses in category 'Food'

Filtered Expenses:
ID | Date       | Amount | Category     | Note
-------------------------------------------------------
 5 | 2025-10-04 | ₹150.00 | Food         | Grocery shopping
-------------------------------------------------------
Filtered Total: ₹150.00

Enter your choice: 7
=== Monthly Summary Options ===
1. All Months Summary
2. Specific Month Summary
3. Year Comparison
4. Back to Main Menu
Choose summary option: 1

=== All Months Summary ===
Month       | Total Spent | Expenses | Avg/Expense
-------------------------------------------------------
Oct 2025    | ₹  2,250.00 |        4 | ₹  562.50
-------------------------------------------------------
TOTAL       | ₹  2,250.00 |        4 | ₹  562.50

Highest spending month: October 2025 (₹2,250.00)
```
```


## Future Enhancements 

Potential features for future versions:
- Export to CSV/Excel
- Date range filtering
- Monthly/yearly reports
- Budget tracking and alerts
- Multiple currency support
- Graphical user interface
- Data backup and restore


