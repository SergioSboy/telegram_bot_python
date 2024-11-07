import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)''')
    conn.commit()
    cur.close()
    conn.close()

def add_user(name):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    cur.close()
    conn.close()