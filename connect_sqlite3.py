import sqlite3

# Database file name (must be in the same folder as this script)
DB_FILE = "college"

def show_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    print("\n📂 Tables in the database:")
    for table in tables:
        print(f"- {table[0]}")

def show_table_data(table_name):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        print(f"\n📄 Data in table '{table_name}':")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"❌ Error: {e}")

    conn.close()

if __name__ == "__main__":
    # Show all tables
    show_tables()

    # Example: Show data from 'students' table (change this if your table has a different name)
    table_to_view = "student"  # <-- change if needed
    show_table_data(table_to_view)



