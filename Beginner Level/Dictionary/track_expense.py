expenses = {
    "you": {"hotel": 0, "food": 0, "transportation": 0, "attractions": 0, "other": 0},
    "partner": {"hotel": 0, "food": 0, "transportation": 0, "attractions": 0, "other": 0}
}

def add_expense(expense_type, amount, payer="you"):
    if payer in expenses and expense_type in expenses[payer]:
        expenses[payer][expense_type] += amount
    else:
        print("Invalid input. Please check expense type or payer.")

def find_total_expense():
    your_total = sum(expenses["you"].values())
    partner_total = sum(expenses["partner"].values())
    return your_total, partner_total

def category_difference():
    diffs = {
        category: expenses["you"][category] - expenses["partner"][category]
        for category in expenses["you"]
    }
    max_category = max(diffs, key=lambda k: abs(diffs[k]))
    return max_category, diffs[max_category]

def main():
    while True:
        expense_type = input("Enter expense type (hotel, food, transportation, attractions, other) or 'exit': ").lower()
        if expense_type == 'exit':
            break
        if expense_type not in expenses["you"]:
            print("Invalid expense type.")
            continue
        try:
            amount = float(input(f"Enter amount for {expense_type}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        payer = input("Who paid? (you/partner): ").lower()
        if payer not in expenses:
            print("Invalid payer.")
            continue
        add_expense(expense_type, amount, payer)

    your_total, partner_total = find_total_expense()
    print(f"\nYour total expenses: ₹{your_total:.2f}")
    print(f"Partner's total expenses: ₹{partner_total:.2f}")
    category, diff = category_difference()
    print(f"Category with the highest difference: '{category}' → ₹{diff:.2f}")

main()