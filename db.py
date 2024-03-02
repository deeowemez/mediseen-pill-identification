import sqlite3  # Import the SQLite library

# Connect to or create the database file
conn = sqlite3.connect("my_database.db")

# Create a cursor object for database operations
cursor = conn.cursor()

# Create a table (if it doesn't already exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
""")

# Insert sample data
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")

# Retrieve and display data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Data in the users table:")
for row in rows:
    print(row)

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()