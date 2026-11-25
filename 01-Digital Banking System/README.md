# Digital Banking System

A simple terminal-based banking application built using Python. I developed this project to apply the Python concepts I have learned and understand how basic banking operations can be implemented through programming.

The system allows multiple users to register accounts, log in using their account number and PIN, and manage their finances through a customer dashboard.

## Features

- Customer account registration
- Automatic generation of unique account numbers
- Four-digit PIN validation
- Account login and logout
- Balance checking
- Deposits and withdrawals
- Money transfers between registered accounts
- Individual transaction history
- Input validation and insufficient funds checks

## Technologies Used

- Python 3.13
- Visual Studio Code

No external libraries or packages are required to run this application.

## Python Concepts Used

- Variables and data types
- Arithmetic and logical operators
- Conditional statements
- For and while loops
- Functions, parameters and return statements
- Lists and list methods
- Tuples
- Dictionaries and nested dictionaries
- String methods
- F-strings
- Input validation

## How to Run

1. Download or clone the repository.
2. Make sure Python is installed on your computer.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

`python main.py`

## Application Menu

```
===== DIGITAL BANKING SYSTEM =====

1. Create Account
2. Login
3. Exit
```

After a successful login, the customer can access the following options:

```
===== CUSTOMER DASHBOARD =====

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Transfer Money
6. Logout
```

## What I Learned

Through this project, I learned how to structure a Python application using separate functions, store and retrieve information from nested dictionaries, validate user inputs and update customer records.

I also gained practical experience in using loops, managing transaction records, passing arguments between functions and identifying and correcting programming errors.

One of the main challenges was understanding how to store multiple customer accounts and update individual account balances without affecting other customer records.

## Current Limitations

- Customer records are stored in temporary memory and are lost when the program closes.
- The application operates through the terminal.
- PINs are stored as plain text for demonstration purposes.
- Transactions support whole-number amounts only.

This project is intended for learning purposes and does not handle real financial transactions.

## Future Improvements

- Permanent storage of customer records
- Database integration
- Secure PIN storage
- Transaction dates and timestamps
- Account statements
- Graphical user interface

## Author

Izaan Mian

Project 01 — Python Portfolio