from core.add import add_expense
from core.view import view_expenses
from core.update import update_expense
from core.delete import delete_expense
from core.summary import show_summary
from core.filter import filter_expenses
from core.monthly import monthly_summary

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Summary Report")
        print("6. Filter Expenses")
        print("7. Monthly Summary")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            filter_expenses()
        elif choice == "7":
            monthly_summary()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()