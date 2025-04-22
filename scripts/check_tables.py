import sqlite3

# Connect to your database using full path
conn = sqlite3.connect(r"C:\Projects\smart-store-robertdavis\data\dw\smart_sales.db")
cursor = conn.cursor()

# Get and print all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in your database:")
for table in tables:
    print(table[0])
