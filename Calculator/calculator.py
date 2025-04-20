def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_input():
    while True:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            return x, y
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def calculator():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4']:
            x, y = get_input()
            
            if choice == '1':
                print(f"{x} + {y} = {add(x, y)}")
            elif choice == '2':
                print(f"{x} - {y} = {subtract(x, y)}")
            elif choice == '3':
                print(f"{x} * {y} = {multiply(x, y)}")
            elif choice == '4':
                print(f"{x} / {y} = {divide(x, y)}")
        else:
            print("Invalid Input! Please choose a valid operation (1-5).")
        
        # Ask if the user wants to continue
        exit_choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if exit_choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator
calculator()
