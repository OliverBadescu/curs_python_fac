from models.database import Database, Expense
from typing import List


class ExpenseController:
    def __init__(self, db_path: str = "expenses.db"):
        self.db = Database(db_path)

    def add_expense(self, amount: float, category: str, description: str, date: str) -> int:
        expense = Expense(
            id=None,
            amount=amount,
            category=category,
            description=description,
            date=date
        )
        return self.db.add_expense(expense)

    def get_all_expenses(self) -> List[Expense]:
        return self.db.get_all_expenses()

    def delete_expense(self, expense_id: int):
        self.db.delete_expense(expense_id)

    def get_category_totals(self, year: int, month: int) -> dict:
        return self.db.get_category_totals(year, month)

    def get_monthly_totals(self, year: int) -> dict:
        return self.db.get_monthly_totals(year)
