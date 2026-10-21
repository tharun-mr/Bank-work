
class Bank:
    minimum_balance = 500

    def __init__(self):
        self.customers = {}
        self.account_number = 1001

    def create_account(self):
        print("\n--- New Customer Registration ---")

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        deposit = float(input("Enter initial deposit: "))

        # Eligibility checking
        if age < 18:
            print("Not eligible: Minimum age is 18.")
            return

        if len(phone) != 10 or not phone.isdigit():
            print("Invalid phone number.")
            return

        if deposit < self.minimum_balance:
            print("Not eligible: Minimum deposit is Rs. 500.")
            return

        account = self.account_number
        self.account_number += 1

        self.customers[account] = {
            "name": name,
            "age": age,
            "phone": phone,
            "address": address,
            "balance": deposit
        }

        print("\nAccount created successfully!")
        print("Account Number:", account)
        print("Customer Name:", name)
        print("Initial Balance: Rs.", deposit)

    def deposit(self):
        account = int(input("Enter account number: "))

        if account not in self.customers:
            print("Account not found.")
            return

        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.customers[account]["balance"] += amount
        print("Deposit successful!")
        print("Balance:", self.customers[account]["balance"])

    def withdraw(self):
        account = int(input("Enter account number: "))

        if account not in self.customers:
            print("Account not found.")
            return

        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        balance = self.customers[account]["balance"]

        if amount > balance:
            print("Insufficient balance.")
        else:
            self.customers[account]["balance"] -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:",
                  self.customers[account]["balance"])

    def check_balance(self):
        account = int(input("Enter account number: "))

        if account in self.customers:
            print("Account Holder:",
                  self.customers[account]["name"])
            print("Current Balance:",
                  self.customers[account]["balance"])
        else:
            print("Account not found.")

    def customer_details(self):
        account = int(input("Enter account number: "))

        if account in self.customers:
            customer = self.customers[account]

            print("\n--- Customer Details ---")
            print("Name:", customer["name"])
            print("Age:", customer["age"])
            print("Phone:", customer["phone"])
            print("Address:", customer["address"])
            print("Account Number:", account)
            print("Balance:", customer["balance"])
        else:
            print("Account not found.")


bank = Bank()

while True:
    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Customer Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        bank.customer_details()
    elif choice == "6":
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid choice. Try again.")
