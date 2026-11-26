"""A terminal-based financial transaction analyzer for learning Python."""

Transactions = []
Budgets = {}
SUSPICIOUS_LIMIT = 100000


# INPUT VALIDATION

def read_text(message):
    """Ask for a non-empty string."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def read_amount(message):
    """Read a positive PKR amount with up to two decimal places."""
    while True:
        value = input(message).strip()
        parts = value.split(".")
        if (len(value) <= 14 and value.isascii()
                and len(parts) <= 2 and parts[0].isdigit()
                and (len(parts) == 1 or
                     (parts[1].isdigit() and len(parts[1]) <= 2))):
            amount = float(value)
            if amount > 0:
                return amount
        print("Enter a positive amount with up to two decimal places (e.g. 1500.50).")


def valid_month(value):
    """Check whether a string represents a valid YYYY-MM month."""
    if (len(value) != 7 or value[4] != "-"
            or not value.isascii()
            or not value[:4].isdigit() or not value[5:].isdigit()):
        return False
    year = int(value[:4])
    month = int(value[5:])
    return year > 0 and 1 <= month <= 12


def valid_date(value):
    """Validate a YYYY-MM-DD date, including leap years."""
    if (len(value) != 10 or value[7] != "-"
            or not valid_month(value[:7]) or not value[8:].isascii()
            or not value[8:].isdigit()):
        return False
    year = int(value[:4])
    month = int(value[5:7])
    day = int(value[8:])
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29
    return 1 <= day <= days[month - 1]


def read_date():
    """Ask for a valid transaction date."""
    while True:
        Date = input("Enter transaction date (YYYY-MM-DD): ").strip()
        if valid_date(Date):
            return Date
        print("Invalid date. Try again.")


def read_month():
    """Ask for the budget month."""
    while True:
        Month = input("Enter budget month (YYYY-MM): ").strip()
        if valid_month(Month):
            return Month
        print("Invalid month. Try again.")


# 1. ADD TRANSACTIONS

def add_transaction():
    """Collect, validate and store one financial transaction."""
    print("\n===== ADD TRANSACTION =====")
    while True:
        Type = input("Enter transaction type (Income/Expense): ").strip().title()
        if Type in ("Income", "Expense"):
            break
        print("Invalid transaction type. Try again.")

    Description = read_text("Enter transaction description: ")
    Category = read_text("Enter transaction category: ").title()
    Amount = read_amount("Enter transaction amount (PKR): ")
    Date = read_date()
    Transaction_ID = len(Transactions) + 1001

    Transaction = {
        "ID": Transaction_ID,
        "Type": Type,
        "Description": Description,
        "Category": Category,
        "Amount": Amount,
        "Date": Date
    }
    Transactions.append(Transaction)
    print("Transaction added successfully!")
    print(f"Transaction ID: {Transaction_ID}")


# 2. VIEW TRANSACTIONS

def print_transaction(Transaction):
    """Display a single transaction in a readable format."""
    print(f"{Transaction['ID']} | {Transaction['Date']} | "
          f"{Transaction['Type']} | {Transaction['Description']} | "
          f"{Transaction['Category']} | PKR {Transaction['Amount']:,.2f}")


def view_transactions():
    """Display all stored transactions."""
    print("\n===== ALL TRANSACTIONS =====")
    if not Transactions:
        print("No transactions recorded.")
    else:
        for Transaction in Transactions:
            print_transaction(Transaction)


# 3. FINANCIAL SUMMARY

def calculate_totals():
    """Return total income, expenses and net savings."""
    Income = 0
    Expenses = 0
    for Transaction in Transactions:
        if Transaction["Type"] == "Income":
            Income += Transaction["Amount"]
        elif Transaction["Type"] == "Expense":
            Expenses += Transaction["Amount"]
    Income = round(Income, 2)
    Expenses = round(Expenses, 2)
    Savings = round(Income - Expenses, 2)
    return Income, Expenses, Savings


def financial_summary():
    """Display totals and savings rate across all recorded dates."""
    Income, Expenses, Savings = calculate_totals()
    print("\n===== FINANCIAL SUMMARY (ALL RECORDS) =====")
    print(f"Total income:   PKR {Income:,.2f}")
    print(f"Total expenses: PKR {Expenses:,.2f}")
    print(f"Net savings:    PKR {Savings:,.2f}")
    if Income > 0:
        Savings_rate = Savings / Income * 100
        print(f"Savings rate:   {Savings_rate:.2f}%")
    else:
        print("Savings rate:   N/A (no income)")


# 4. CATEGORY ANALYSIS

def category_totals(Month=""):
    """Return expense totals by category, optionally for one month."""
    Categories = {}
    for Transaction in Transactions:
        if Transaction["Type"] == "Expense":
            if Month == "" or Transaction["Date"][:7] == Month:
                Category = Transaction["Category"]
                Amount = Transaction["Amount"]
                Categories[Category] = round(Categories.get(Category, 0) + Amount, 2)
    return Categories


def category_analysis():
    """Display total expense and spending share for each category."""
    print("\n===== EXPENSE CATEGORY ANALYSIS =====")
    Categories = category_totals()
    if not Categories:
        print("No expenses recorded.")
        return
    Total = sum(Categories.values())
    for Category, Amount in Categories.items():
        Percentage = Amount / Total * 100
        print(f"{Category}: PKR {Amount:,.2f} ({Percentage:.2f}%)")


# 5. HIGHEST AND LOWEST EXPENSES

def expense_extremes():
    """Find the highest and lowest individual expenses using a loop."""
    Highest = None
    Lowest = None
    for Transaction in Transactions:
        if Transaction["Type"] == "Expense":
            if Highest is None or Transaction["Amount"] > Highest["Amount"]:
                Highest = Transaction
            if Lowest is None or Transaction["Amount"] < Lowest["Amount"]:
                Lowest = Transaction
    return Highest, Lowest


def highest_lowest_expenses():
    """Display the largest and smallest expense records."""
    print("\n===== HIGHEST AND LOWEST EXPENSES =====")
    Highest, Lowest = expense_extremes()
    if Highest is None:
        print("No expenses recorded.")
    else:
        print("Highest expense:")
        print_transaction(Highest)
        print("Lowest expense:")
        print_transaction(Lowest)


# 6. BUDGET MONITORING

def set_budget():
    """Set or replace a category budget for a particular month."""
    Month = read_month()
    Category = read_text("Enter expense category: ").title()
    Limit = read_amount("Enter monthly budget (PKR): ")
    Budgets[(Month, Category)] = Limit
    print(f"Budget saved: {Month} | {Category} | PKR {Limit:,.2f}")


def budget_status(Month, Category):
    """Return budget limit, actual spending and remaining budget."""
    Limit = Budgets[(Month, Category)]
    Actual = category_totals(Month).get(Category, 0)
    Remaining = round(Limit - Actual, 2)
    return Limit, Actual, Remaining


def view_budgets():
    """Compare recorded monthly category spending with saved budgets."""
    print("\n===== BUDGET PERFORMANCE =====")
    if not Budgets:
        print("No budgets set.")
        return
    for Month, Category in Budgets:
        Limit, Actual, Remaining = budget_status(Month, Category)
        print(f"{Month} | {Category}")
        print(f"Budget: PKR {Limit:,.2f} | Spent: PKR {Actual:,.2f}")
        if Remaining < 0:
            print(f"Over budget by PKR {-Remaining:,.2f}")
        else:
            print(f"Remaining budget: PKR {Remaining:,.2f}")


def budget_monitoring():
    """Display the budget menu until the user returns."""
    while True:
        print("\n1. Set or update a monthly category budget")
        print("2. View budget performance")
        print("3. Back to main menu")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                set_budget()
            case "2":
                view_budgets()
            case "3":
                break
            case _:
                print("Invalid choice. Please try again.")


# 7. DUPLICATE DETECTION

def find_duplicates():
    """Find later records matching an earlier transaction's details."""
    Seen = set()
    Duplicates = []
    for Transaction in Transactions:
        Signature = (
            Transaction["Type"],
            Transaction["Description"].lower(),
            Transaction["Category"].lower(),
            Transaction["Amount"],
            Transaction["Date"]
        )
        if Signature in Seen:
            Duplicates.append(Transaction)
        else:
            Seen.add(Signature)
    return Duplicates


def detect_duplicates():
    """Display possible duplicates without removing any records."""
    print("\n===== POTENTIAL DUPLICATES =====")
    Duplicates = find_duplicates()
    if not Duplicates:
        print("No potential duplicates found.")
    else:
        for Transaction in Duplicates:
            print_transaction(Transaction)
        print(f"Potential duplicate records: {len(Duplicates)}")
        print("Review these records manually; matching details may be legitimate.")


# 8. SUSPICIOUS TRANSACTIONS

def find_suspicious():
    """Flag income or expenses at or above the configured threshold."""
    Flagged = []
    for Transaction in Transactions:
        if Transaction["Amount"] >= SUSPICIOUS_LIMIT:
            Flagged.append(Transaction)
    return Flagged


def detect_suspicious():
    """Display large transactions for review, not as proof of fraud."""
    print("\n===== LARGE TRANSACTION ALERTS =====")
    print(f"Review threshold: PKR {SUSPICIOUS_LIMIT:,.2f}")
    Flagged = find_suspicious()
    if not Flagged:
        print("No transactions meet the review threshold.")
    else:
        for Transaction in Flagged:
            print_transaction(Transaction)
        print(f"Flagged records: {len(Flagged)}")
        print("Large amounts alone do not establish fraud.")


# 9. SEARCH TRANSACTIONS

def find_transactions(Keyword):
    """Find records matching an ID, description, category, type or date."""
    Keyword = Keyword.strip().lower()
    Results = []
    if not Keyword:
        return Results
    for Transaction in Transactions:
        if (Keyword in str(Transaction["ID"])
                or Keyword in Transaction["Description"].lower()
                or Keyword in Transaction["Category"].lower()
                or Keyword in Transaction["Type"].lower()
                or Keyword in Transaction["Date"]):
            Results.append(Transaction)
    return Results


def search_transactions():
    """Ask for a search term and display matching transactions."""
    print("\n===== SEARCH TRANSACTIONS =====")
    Keyword = read_text("Enter ID, description, category, type or date: ")
    Results = find_transactions(Keyword)
    if not Results:
        print("No matching transactions found.")
    else:
        for Transaction in Results:
            print_transaction(Transaction)
        print(f"Matching transactions: {len(Results)}")


# 10. FINANCIAL REPORT

def generate_report():
    """Combine existing analytical functions into one terminal report."""
    print("\n========== FINANCIAL REPORT ==========")
    print(f"Total transaction records: {len(Transactions)}")
    financial_summary()
    category_analysis()
    highest_lowest_expenses()
    view_budgets()
    detect_duplicates()
    detect_suspicious()
    print("\n========== END OF REPORT ==========")


# 11. MAIN MENU

def menu():
    """Run the application until the user chooses to exit."""
    while True:
        print("\n====Welcome to the Financial Transaction Analyzer====")
        print("1. Add Transactions")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Category Analysis")
        print("5. Highest and Lowest Expenses")
        print("6. Budget Monitoring")
        print("7. Detect Duplicate Transactions")
        print("8. Detect Suspicious Transactions")
        print("9. Search Transactions")
        print("10. Generate Financial Report")
        print("11. Exit")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                add_transaction()
            case "2":
                view_transactions()
            case "3":
                financial_summary()
            case "4":
                category_analysis()
            case "5":
                highest_lowest_expenses()
            case "6":
                budget_monitoring()
            case "7":
                detect_duplicates()
            case "8":
                detect_suspicious()
            case "9":
                search_transactions()
            case "10":
                generate_report()
            case "11":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


# Start the menu only when this file is run directly.
if __name__ == "__main__":
    menu()
