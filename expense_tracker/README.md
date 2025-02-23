# Expense Tracker System
A simple but powerful expense tracking system implemented in Python, designed as part of the semester project to demonstrate object-oriented programming concepts.
Project Description
This project implements two main classes:

Expense: Represents individual financial expenses
ExpenseDB: Manages a collection of expenses

Key Features

Create and manage expenses with titles and amounts
Auto-generated UUID for each expense
UTC timestamp tracking for creation and updates
Search functionality by ID or title
Dictionary conversion for data serialization

Getting Started
Prerequisites

Python 3.6 or higher

Installation

Clone this repository

git clone [https://github.com/teezliz/teezliz_altschool/expense_tracker.git](https://github.com/teezliz/teezliz_altschool/tree/main/expense_tracker)

Navigate to project directory

bashCopycd expense-tracker
Usage Example
pythonCopy# Create an expense database
db = ExpenseDB()

# Create a new expense
expense = Expense("Groceries", 50.00)

# Add expense to database
db.add_expense(expense)

# Update expense
expense.update(amount=55.00)

# Get all expenses with title "Groceries"
groceries = db.get_expenses_by_title("Groceries")

# Convert all expenses to dictionary format
all_expenses = db.to_dict()
Class Documentation
Expense Class

_init_(title: str, amount: float): Initialize a new expense
update(title: str = None, amount: float = None): Update expense details
to_dict(): Convert expense to dictionary format

ExpenseDB Class

add_expense(expense: Expense): Add new expense to database
remove_expense(expense_id: str): Remove expense by ID
get_expense_by_id(expense_id: str): Retrieve specific expense
get_expenses_by_title(title: str): Get all expenses with matching title
to_dict(): Convert all expenses to list of dictionaries

Project Structure
`expense-tracker/main.py   # Main implementation file`
`expense-tracker/README.md # Project documentation`

Author
[Elizabeth Ogundipe]
