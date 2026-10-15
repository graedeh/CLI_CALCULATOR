def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():
    print("\n===== CLI CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose 1-5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = (input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print("Result:", result)


if __name__ == "__main__":
    calculator()