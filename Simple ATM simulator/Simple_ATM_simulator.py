balance = 10000


def check_balance():
    print(f"\n💰 Your current balance is: ₹{balance}")


def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("⚠️ Please enter a positive amount.")
        else:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
            check_balance()
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")


def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("⚠️ Please enter a positive amount.")
        elif amount > balance:
            print("❌ Insufficient balance.")
        else:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            check_balance()
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")


def atm_menu():
    while True:
        print("\n===== 🏧 ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 4.")


# Start the ATM
print("🛡️ Welcome to the Python ATM Simulator!")
atm_menu()
