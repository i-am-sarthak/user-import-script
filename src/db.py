import sqlite3
import os

def get_connection(db_path):
    """Returns a SQLite connection object."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database(conn, schema_path):
    """Create users table"""

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor = conn.cursor()
    try:
        cursor.executescript(schema_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        raise


def upsert_user(conn, user):
    """Insert or update a user record based on username"""
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Users (accountnumber, username, emailaccount, phonenumber, address, password)
        VALUES (:accountnumber, :username, :emailaccount, :phonenumber, :address, :password)
        ON CONFLICT(username) DO UPDATE SET
            accountnumber = excluded.accountnumber,
            emailaccount = excluded.emailaccount,
            phonenumber = excluded.phonenumber,
            address = excluded.address,
            password = excluded.password;
    """, user)

    conn.commit()
