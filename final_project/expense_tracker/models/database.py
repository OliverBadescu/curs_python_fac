import sqlite3
from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Expense:
    id: Optional[int]
    amount: float
    category: str
    description: str
    date: str


CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Utilities",
    "Shopping",
    "Health",
    "Other"
]


class Database:
    def __init__(self, db_path: str = "expenses.db"):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_expense(self, expense: Expense) -> int:
        with self._get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                (expense.amount, expense.category, expense.description, expense.date)
            )
            conn.commit()
            return cursor.lastrowid

    def get_all_expenses(self) -> List[Expense]:
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, amount, category, description, date FROM expenses ORDER BY date DESC"
            )
            return [Expense(*row) for row in cursor.fetchall()]

    def delete_expense(self, expense_id: int):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

    def get_expenses_by_month(self, year: int, month: int) -> List[Expense]:
        month_str = f"{year}-{month:02d}"
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, amount, category, description, date FROM expenses WHERE date LIKE ?",
                (f"{month_str}%",)
            )
            return [Expense(*row) for row in cursor.fetchall()]

    def get_category_totals(self, year: int, month: int) -> dict:
        expenses = self.get_expenses_by_month(year, month)
        totals = {}
        for exp in expenses:
            totals[exp.category] = totals.get(exp.category, 0) + exp.amount
        return totals

    def get_monthly_totals(self, year: int) -> dict:
        with self._get_connection() as conn:
            cursor = conn.execute(
                """SELECT strftime('%m', date) as month, SUM(amount)
                   FROM expenses
                   WHERE strftime('%Y', date) = ?
                   GROUP BY month ORDER BY month""",
                (str(year),)
            )
            return {int(row[0]): row[1] for row in cursor.fetchall()}
