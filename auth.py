import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta, timezone
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

def create_otc(email: str):
    """Generate and store a one-time code for a registered user."""

    # 1. Find the user
    user = get_user_by_email(email)

    if not user:
        return None

    # 2. Generate a secure 6-digit OTC
    otc = f"{secrets.randbelow(1_000_000):06d}"

    # 3. Hash the OTC before storing it
    otc_hash = hashlib.sha256(otc.encode()).hexdigest()

    # 4. Set an expiry time (10 minutes)
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=10)

    # 5. Store the hash and expiry in the database
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO otc (user_id, otc_hash, expires_at)
            VALUES (?, ?, ?)
            """,
            (user["user_id"], otc_hash, expires_at.isoformat())
        )
        conn.commit()

    # Return the plain OTC for now.
    # Later this will be sent by email instead.
    return otc
