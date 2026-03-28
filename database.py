import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "data/expenses.db"

def get_connection():
    # Ensure data directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Transactions Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            subcategory TEXT,
            description TEXT,
            payment_method TEXT,
            tags TEXT
        )
    ''')
    
    # Create Budgets Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            monthly_limit REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def add_transaction(date, amount, category, subcategory="", description="", payment_method="cash", tags=""):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, amount, category, subcategory, description, payment_method, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, amount, category, subcategory, description, payment_method, tags))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM transactions ORDER BY date DESC", conn)
    conn.close()
    return df

def set_budget(category, monthly_limit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO budgets (category, monthly_limit)
        VALUES (?, ?)
    ''', (category, monthly_limit))
    conn.commit()
    conn.close()

def get_all_budgets():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM budgets", conn)
    conn.close()
    return dict(zip(df['category'], df['monthly_limit'])) if not df.empty else {}

if __name__ == "__main__":
    init_db()
