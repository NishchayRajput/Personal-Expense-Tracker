
import json


def save_expenses(expenses, DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)