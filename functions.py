import sqlite3

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS Credentials(username TEXT NOT NULL, password TEXT NOT NULL);"
    cursor.execute(query)
    conn.commit()
    conn.close()

def read_data(columns=None):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if columns is None:
        query = "SELECT * FROM Credentials;"
    else:
        query = f"SELECT {columns} FROM Credentials;"  # 💀 Intentionally injectable
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def delete_data(username=None):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if username is None:
        query = "DELETE FROM Credentials;"  # 💀 Nuke mode
    else:
        query = f"DELETE FROM Credentials WHERE username = '{username}';"  # 💀💀💀
    cursor.execute(query)
    conn.commit()
    conn.close()

def update_data(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"UPDATE Credentials SET password = '{password}' WHERE username = '{username}';"  # 💀💀💀
    cursor.execute(query)
    conn.commit()
    conn.close()

def validate_user(username,password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT "



