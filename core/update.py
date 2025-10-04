
from utility.load import load_expenses
from utility.save import save_expenses
from core.view import view_expenses
from datetime import datetime
from config import DATA_FILE

def update_expense():
    expenses = load_expenses(DATA_FILE)
    view_expenses()
    try:
        expense_id = int(input("Enter expense ID to update: "))
        expense = next((exp for exp in expenses if exp["id"] == expense_id), None)
        if not expense:
            print("Expense not found.")
            return

        print("Leave blank to keep current value.")
        new_amount = input(f"Amount ({expense['amount']}): ").strip()
        new_date = input(f"Date ({expense['date']}): ").strip()
        new_note = input(f"Note ({expense['note']}): ").strip()
        new_category = input(f"Category ({expense['category']}): ").strip()

        if new_amount:
            expense["amount"] = float(new_amount)
        if new_date:
            datetime.strptime(new_date, "%Y-%m-%d")
            expense["date"] = new_date
        if new_note:
            expense["note"] = new_note
        if new_category:
            expense["category"] = new_category

        save_expenses(expenses, DATA_FILE)
        print("Expense updated successfully!")
    except ValueError:
        print("Invalid input.")
