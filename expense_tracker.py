from datetime import datetime
import logging
import sqlite3

# Setup Automated Logging & Exception Safety
logging.basicConfig(
    filename='expense_tracker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            ''')
            conn.commit()
            conn.close()
            logging.info("Database initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing database: {e}")

    def add_expense(self, title: str, amount: float, category: str):
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
                           (title, amount, category, date_str))
            conn.commit()
            conn.close()
            logging.info(f"Added expense: {title} of amount {amount}")
            print(f"Expense '{title}' added successfully!")
        except Exception as e:
            logging.error(f"Failed to add expense: {e}")
            print(f"Error: {e}")

    def view_expenses(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            rows = cursor.fetchall()
            conn.close()
            
            print("\n--- All Expenses ---")
            for row in rows:
                print(f"ID: {row[0]} | Title: {row[1]} | Amount: ₹{row[2]:.2f} | Category: {row[3]} | Date: {row[4]}")
            print("-" * 30)
        except Exception as e:
            logging.error(f"Error viewing expenses: {e}")

    def total_spending(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(amount) FROM expenses")
            total = cursor.fetchone()[0]
            conn.close()
            return total if total else 0.0
        except Exception as e:
            logging.error(f"Error calculating total spending: {e}")
            return 0.0

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Groceries", 1250.50, "Food")
    tracker.add_expense("Electricity Bill", 2400.00, "Utilities")
    tracker.view_expenses()
    print(f"Total Spending: ₹{tracker.total_spending():.2f}")
    
