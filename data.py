import sqlite3

# Connect to a local database file (or use ':memory:' for an in-memory DB)
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

DB_PATH = "app.db"

# Enable foreign key enforcement in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# 1. Create the 'users' table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
)

# 2. Create the 'otc' (One-Time Code) table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS otc (
    otc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    otc_hash TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);
"""
)

conn.commit()


# function to convert users table to dataframe, this is imported in app.py

def get_users_df():
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            "SELECT user)id, name, email, is_active FROM users", conn
        )
