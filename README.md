# Book-Management-Project
This is a simple Bank Management System developed in Python that uses a JSON file to store user data. It supports account creation, deposits, withdrawals, account details display, updates, and deletion of accounts via a console-based interface.

## 🧠 Features
- Create a new account (for users 18+ with a 4-digit PIN)

- Deposit money to an account

- Withdraw money from an account (if sufficient balance)

- View account details

- Update name, email, or PIN

- Delete account

All data is stored in a persistent JSON file


## 🔧 How It Works
The program reads and writes to a file data.json inside the Bank Management Project folder. It uses Python’s built-in json, random, and string modules.

Each account includes:

Name

Age

Email

Account Number (randomly generated with letters, digits, and special characters)

4-digit PIN

Bank Balance
