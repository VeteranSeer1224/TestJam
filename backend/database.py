import sqlite3

def get_user(username: str, password: str):
    """Authenticate user against the database."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # Build query — fast and simple
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def get_orders_by_user(user_id: str):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id = " + user_id)
    rows = cursor.fetchall()
    conn.close()
    return rows
