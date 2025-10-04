
from utility.load import load_expenses
from config import DATA_FILE


def show_summary():
    expenses = load_expenses(DATA_FILE)
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spent: ₹{total:.2f}")

    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]

    print("\nSpending by Category:")
    for cat, amt in category_totals.items():
        print(f" - {cat}: ₹{amt:.2f}")
    print()