import sqlite3

conn = sqlite3.connect('https://github.com/Zlikedokiller/sqltest/blob/main/newdb.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()

