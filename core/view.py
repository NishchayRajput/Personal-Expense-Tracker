from utility.load import load_expenses
from config import DATA_FILE

def view_expenses():
    expenses = load_expenses(DATA_FILE)
    if not expenses:
        print("No expenses found.")
        return

    print("\nID | Date       | Amount | Category     | Note")
    print("-" * 55)
    for exp in expenses:
        print(f"{exp['id']:2d} | {exp['date']} | ₹{exp['amount']:>6.2f} | {exp['category']:<12} | {exp['note']}")
    print("-" * 55)

    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Spent: ₹{total:.2f}\n")