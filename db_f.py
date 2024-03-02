import sqlite3  # Import the SQLite library

# Connect to or create the database file
conn = sqlite3.connect("pill_info.db")

# Create a cursor object for database operations
cursor = conn.cursor()

# Retrieve and display data
cursor.execute("SELECT * FROM pill_info_table")
rows = cursor.fetchall()
print("Data in the users table:")
for row in rows:
    print(row)

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()