import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initialize an Expense object.
        
        Args:
            title (str): The title of the expense
            amount (float): The amount of the expense
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None) -> None:
        """
        Update the expense title and/or amount.
        
        Args:
            title (str, optional): New title for the expense
            amount (float, optional): New amount for the expense
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self) -> dict:
        """
        Convert the expense object to a dictionary.
        
        Returns:
            dict: Dictionary representation of the expense
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class ExpenseDB:
    def __init__(self):
        """Initialize an empty expense database."""
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        """
        Add an expense to the database.
        
        Args:
            expense (Expense): The expense object to add
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> bool:
        """
        Remove an expense from the database by ID.
        
        Args:
            expense_id (str): The ID of the expense to remove
            
        Returns:
            bool: True if expense was removed, False if not found
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                return True
        return False

    def get_expense_by_id(self, expense_id: str) -> Expense:
        """
        Get an expense by its ID.
        
        Args:
            expense_id (str): The ID of the expense to retrieve
            
        Returns:
            Expense: The expense object if found, None otherwise
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title: str) -> list:
        """
        Get all expenses with a given title.
        
        Args:
            title (str): The title to search for
            
        Returns:
            list: List of expense objects with matching title
        """
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self) -> list:
        """
        Convert all expenses to a list of dictionaries.
        
        Returns:
            list: List of dictionaries representing all expenses
        """
        return [expense.to_dict() for expense in self.expenses]


# Example usage:
if __name__ == "__main__":
    # Create an expense database
    db = ExpenseDB()
    
    # Create some expenses
    expense1 = Expense("Lunch", 10.50)
    expense2 = Expense("Books", 50.00)
    expense3 = Expense("Lunch", 15.75)
    
    # Add expenses to database
    db.add_expense(expense1)
    db.add_expense(expense2)
    db.add_expense(expense3)
    
    # Update an expense
    expense1.update(amount=12.50)
    
    # Get expenses by title
    lunch_expenses = db.get_expenses_by_title("Lunch")
    print("Lunch expenses:", [exp.to_dict() for exp in lunch_expenses])
    
    # Get expense by ID
    expense = db.get_expense_by_id(expense2.id)
    if expense:
        print("Found expense:", expense.to_dict())
    
    # Remove an expense
    db.remove_expense(expense3.id)
    
    # Print all expenses
    print("All expenses:", db.to_dict())