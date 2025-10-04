
import datetime
from utility.load import load_expenses
from utility.save import save_expenses
from utility.generateId import generate_id
from config import DATA_FILE

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if date_str == "":
            date_str = datetime.datetime.today().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date_str, "%Y-%m-%d") 
        note = input("Enter note/description: ").strip()
        category = input("Enter category (optional): ").strip() or "General"

        expenses = load_expenses(DATA_FILE)
        new_expense = {
            "id": generate_id(expenses),
            "amount": amount,
            "date": date_str,
            "note": note,
            "category": category
        }
        expenses.append(new_expense)
        save_expenses(expenses, DATA_FILE)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid input. Please try again.")
