# Personal Expense Tracker - Technical Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Design Assumptions](#design-assumptions)
3. [Architecture & Design](#architecture--design)
4. [Data Model](#data-model)
5. [Sample Inputs/Outputs](#sample-inputsoutputs)
6. [Error Handling](#error-handling)
7. [Performance Considerations](#performance-considerations)

## System Overview

The Personal Expense Tracker is a command-line application built in Python that allows users to manage their financial expenses. The system provides CRUD operations, filtering capabilities, and comprehensive reporting features.

**Core Features:**
- Expense management (Add, View, Update, Delete)
- Advanced filtering (by date range, category, or both)
- Monthly summaries with year-over-year comparisons
- Data persistence using JSON format

## Design Assumptions

### 1. Data Storage
- **Single-user system**: Designed for individual use, not multi-user concurrent access
- **Local storage**: Data is stored locally in JSON format for simplicity and portability
- **File-based persistence**: No database required, making it lightweight and easy to deploy

### 2. Data Format
- **Currency**: All amounts are stored as floating-point numbers (assumes single currency)
- **Date format**: ISO format (YYYY-MM-DD) for consistency and sorting
- **ID generation**: Sequential integer IDs starting from 1
- **Categories**: Case-insensitive string matching for category operations

### 3. User Interface
- **Command-line interface**: Text-based menu system for universal compatibility
- **Single-session operations**: Each operation completes before returning to main menu
- **Error recovery**: Invalid inputs return user to previous menu level

### 4. Performance
- **Small to medium datasets**: Optimized for personal use (hundreds to thousands of expenses)
- **In-memory processing**: Entire dataset loaded into memory for operations
- **File I/O per operation**: Data saved after each modification

## Architecture & Design

### Modular Structure
```
├── main.py              # Application entry point and menu system
├── config.py            # Configuration constants (DATA_FILE path)
├── core/                # Business logic modules
│   ├── add.py          # Expense creation
│   ├── view.py         # Expense display
│   ├── update.py       # Expense modification
│   ├── delete.py       # Expense removal
│   ├── summary.py      # Basic reporting
│   ├── filter.py       # Advanced filtering
│   └── monthly.py      # Monthly analysis
└── utility/            # Shared utility functions
    ├── load.py         # Data loading from JSON
    ├── save.py         # Data saving to JSON
    └── generateId.py   # Unique ID generation
```

### Design Patterns

**1. Separation of Concerns**
- Each module handles a specific domain of functionality
- Utility functions separated from business logic
- Configuration isolated in dedicated module

**2. Single Responsibility Principle**
- Each function performs one specific task
- Clear function naming conventions
- Minimal parameter passing

**3. Error Handling Strategy**
- Graceful degradation on invalid inputs
- User-friendly error messages
- Return to safe state (main menu) on errors

## Data Model

### Expense Record Structure
```json
{
    "id": 1,
    "amount": 250.50,
    "date": "2025-10-04",
    "note": "Lunch at restaurant",
    "category": "Food"
}
```

**Field Specifications:**
- `id` (integer): Unique identifier, auto-generated sequentially
- `amount` (float): Positive number representing expense amount
- `date` (string): ISO date format (YYYY-MM-DD)
- `note` (string): User description, mandatory field
- `category` (string): Optional categorization, defaults to "General"

### Data File Format
```json
[
    {
        "id": 1,
        "amount": 250.50,
        "date": "2025-10-04",
        "note": "Lunch at restaurant",
        "category": "Food"
    },
    {
        "id": 2,
        "amount": 1500.00,
        "date": "2025-10-04",
        "note": "Monthly groceries",
        "category": "Food"
    }
]
```

## Sample Inputs/Outputs

### 1. Adding an Expense
**Input:**
```
Enter amount: 250.50
Enter date (YYYY-MM-DD) or leave blank for today: 2025-10-04
Enter note/description: Lunch at restaurant
Enter category (optional): Food
```

**Output:**
```
Expense added successfully!
```

**Generated Record:**
```json
{
    "id": 3,
    "amount": 250.50,
    "date": "2025-10-04",
    "note": "Lunch at restaurant",
    "category": "Food"
}
```

### 2. Filtering by Category
**Input:**
```
Choose filter option: 2
Available categories:
1. Food
2. Transport
3. Entertainment
Enter category number or type category name: Food
```

**Output:**
```
Found 5 expenses in category 'Food'

Filtered Expenses:
ID | Date       | Amount | Category     | Note
-------------------------------------------------------
 1 | 2025-10-01 | ₹  50.00 | Food         | Coffee
 3 | 2025-10-04 | ₹ 250.50 | Food         | Lunch at restaurant
 5 | 2025-10-05 | ₹ 120.00 | Food         | Breakfast
 7 | 2025-10-07 | ₹ 300.00 | Food         | Dinner
 9 | 2025-10-09 | ₹ 180.75 | Food         | Snacks
-------------------------------------------------------
Filtered Total: ₹901.25

Category Breakdown:
 - Food: ₹901.25
```

### 3. Monthly Summary
**Input:**
```
Choose summary option: 2
Enter year (YYYY): 2025
Enter month (1-12): 10
```

**Output:**
```
=== October 2025 Detailed Summary ===
Total Spent: ₹3,450.75
Number of Expenses: 15
Average per Expense: ₹230.05

Category Breakdown:
 - Food        : ₹ 1,250.50 ( 36.2%)
 - Transport   : ₹   890.25 ( 25.8%)
 - Entertainment: ₹   680.00 ( 19.7%)
 - Shopping    : ₹   630.00 ( 18.3%)

Daily Spending:
 - 2025-10-01 (Sun): ₹150.00
 - 2025-10-02 (Mon): ₹420.75
 - 2025-10-03 (Tue): ₹180.00
 - 2025-10-04 (Wed): ₹550.50
 - 2025-10-05 (Thu): ₹290.25

 Highest spending day: 2025-10-04 (Wednesday) - ₹550.50
```

### 4. Year-over-Year Comparison
**Input:**
```
Choose summary option: 3
```

**Output:**
```
=== Year-over-Year Comparison ===
Month    | 2024     | 2025     
---------------------------------
Jan      | ₹  2,340 | ₹  2,890 
Feb      | ₹  2,150 | ₹  2,650 
Mar      | ₹  2,890 | ₹  3,200 
Apr      | ₹  2,450 | ₹  2,890 
May      | ₹  3,200 | ₹    -   
Jun      | ₹  2,780 | ₹    -   
---------------------------------
TOTAL    | ₹ 16,810 | ₹ 11,630 

 YoY Growth (2024 to 2025): +12.5%
```

## Error Handling

### Input Validation
**Invalid Amount:**
```
Enter amount: -50
Amount must be positive.
```

**Invalid Date:**
```
Enter date (YYYY-MM-DD): 2025-13-45
Invalid date format. Please use YYYY-MM-DD.
```

**Non-existent Expense ID:**
```
Enter expense ID to update: 999
Expense not found.
```

### File Operations
**Missing Data File:**
- Application creates empty expense list
- No error message shown to user
- Graceful handling of first-time usage

**Corrupted JSON:**
- Returns empty list
- Logs error internally
- Continues operation with fresh start

## Performance Considerations

### Time Complexity
- **Add Operation**: O(n) for ID generation, O(1) for append
- **View Operations**: O(n) for display formatting
- **Filter Operations**: O(n) for filtering, O(n log n) for sorting
- **Monthly Analysis**: O(n) for grouping, O(k) for display (k = number of groups)

### Memory Usage
- **Full dataset in memory**: Suitable for personal use (< 10MB typically)
- **No caching**: Fresh load on each operation
- **Temporary collections**: Created for filtering and grouping operations

### File I/O
- **Read on startup**: Full file read into memory
- **Write on modification**: Complete file rewrite after changes
- **No incremental updates**: Ensures data consistency

### Optimization Opportunities
1. **Caching**: Keep data in memory between operations
2. **Incremental updates**: Append-only file format for new records
3. **Indexing**: Create indexes for frequently filtered fields
4. **Compression**: Use compressed JSON for large datasets

## Scalability Considerations

### Current Limitations
- **Single-user**: No concurrent access support
- **Memory bound**: All data loaded into memory
- **File locking**: No protection against concurrent file access

### Future Enhancements
- **Database backend**: SQLite for better performance and querying
- **Pagination**: For large datasets in view operations
- **Background processing**: For complex analytical operations
- **Data compression**: For historical data archival

---

**Author**: Personal Expense Tracker Development Team  
**Version**: 1.0  
**Last Updated**: October 2025
