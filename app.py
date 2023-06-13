import sqlite3

def add_numbers(a, b):
    return a + b

def get_user_by_id(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM users WHERE id={user_id}")

    user = c.fetchone()
    conn.close()
    return user

