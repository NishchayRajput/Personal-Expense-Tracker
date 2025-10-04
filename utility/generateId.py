
def generate_id(expenses):
    if not expenses:
        return 1
    return max(exp["id"] for exp in expenses) + 1