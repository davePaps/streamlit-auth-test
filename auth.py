import sqlite3
from db import get_connection


def add_user(name: str, email: str) -> bool:
    """Inserts a user into SQLite. Returns True on success, False if email exists."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        # Handles UNIQUE constraint failure on email
        return False


def get_user_by_email(email: str):
    """Fetches a single user record as a dictionary-like object."""
    with get_connection() as conn:
        cursor = conn.cursor()
        user = cursor.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        return dict(user) if user else None


def get_all_users():
    """Fetches all users for admin or display view."""
    with get_connection() as conn:
        cursor = conn.cursor()
        users = cursor.execute(
            "SELECT user_id, name, email, is_active, created_at FROM users"
        ).fetchall()
        return [dict(u) for u in users]
