import sqlite3

conn = sqlite3.connect('newdb.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

result = []

def request():
    for row in results:
        results.append(row)

conn.close()

print(results)
