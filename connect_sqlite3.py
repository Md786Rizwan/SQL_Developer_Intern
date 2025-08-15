import sqlite3

# Connect to the database
conn = sqlite3.connect("college.sqlite3")

# Create a cursor
cursor = conn.cursor()

# Example: Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Example: Read data from a table (if 'students' exists)
# cursor.execute("SELECT * FROM students")
# print(cursor.fetchall())

conn.close()
