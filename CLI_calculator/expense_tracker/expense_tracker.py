def add_expense(expenses):
    description = input("Enter expense description: ").strip()

    if not description:
        print("Error: Description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in naira: "))

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid number.")
        return

    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== YOUR EXPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} - "
            f"₦{expense['amount']:.2f}"
        )


def show_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ₦{total:.2f}")


def main():
    expenses = []

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "q":
            print("Thank you for using the expense tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()