
from utility.load import load_expenses
from utility.save import save_expenses
from core.view import view_expenses
from config import DATA_FILE

def delete_expense():
    expenses = load_expenses(DATA_FILE)
    view_expenses()
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        new_expenses = [exp for exp in expenses if exp["id"] != expense_id]
        if len(new_expenses) == len(expenses):
            print("Expense not found.")
            return
        save_expenses(new_expenses, DATA_FILE)
        print("Expense deleted successfully!")
    except ValueError:
        print("Invalid input.")