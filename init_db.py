import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# สร้าง table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
""")

# mock data
users = [
    ("alice", "alice@example.com", "password123"),
    ("bob", "bob@example.com", "secret456"),
    ("charlie", "charlie@example.com", "mypassword")
]

cursor.executemany(
    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
    users
)

conn.commit()
conn.close()

print("users.db created with mock data")