accounts = {}


# ACCOUNT CREATION
def create_account():
    print("\n===== CREATE ACCOUNT =====")

    while True:
        Username = input("Enter Your Name: ").strip()

        if Username != "":
            break
        else:
            print("Name cannot be empty.")

    while True:
        Password = input("Enter Your Four Digit PIN: ")

        if len(Password) == 4 and Password.isdigit() and Password.isascii():
            print("Valid PIN")
            break
        else:
            print("Invalid PIN. Try again.")

    Account_number = len(accounts) + 1001
    Balance = 0
    Transaction = []

    Account = {
        "Username": Username,
        "Password": Password,
        "Balance": Balance,
        "Account Number": Account_number,
        "Transaction History": Transaction
    }

    accounts[Account_number] = Account

    print("\nAccount created successfully!")
    print(f"Account holder: {Username}")
    print(f"Account number: {Account_number}")
    print(f"Balance: PKR {Balance}")


# CUSTOMER DASHBOARD
def dashboard(Account_number):

    while True:
        print("\n===== CUSTOMER DASHBOARD =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Transfer Money")
        print("6. Logout")

        Select_option = input("Enter your Choice: ")

        if Select_option == "1":
            print("Checking balance...")

        elif Select_option == "2":
            print("Depositing money...")

        elif Select_option == "3":
            print("Withdrawing money...")

        elif Select_option == "4":
            print("Viewing transaction history...")

        elif Select_option == "5":
            print("Transferring money...")

        elif Select_option == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice. Try again.")


# CUSTOMER LOGIN
def login():
    print("\n===== CUSTOMER LOGIN =====")

    while True:
        Account_number = input("Enter Your Account Number: ")

        if Account_number.isdigit() and Account_number.isascii() and len(Account_number) <= 20:
            Account_number = int(Account_number)
            break
        else:
            print("Please enter a valid account number.")

    if Account_number in accounts:

        Password = input("Enter Your PIN: ")

        if Password == accounts[Account_number]["Password"]:

            Username = accounts[Account_number]["Username"]

            print("Login successful!")
            print(f"Welcome, {Username}")

            dashboard(Account_number)

        else:
            print("Incorrect PIN")

    else:
        print("Account not found")


# MAIN MENU
while True:
    print("\n===== DIGITAL BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    Choice = input("Enter your Choice: ")

    if Choice == "1":
        create_account()

    elif Choice == "2":
        login()

    elif Choice == "3":
        print("Thank you for using our banking system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")