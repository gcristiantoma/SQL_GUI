import sqlite3
my_conn = sqlite3.connect('my_db.db')
print("Created database successfully");

print(my_conn.execute('''select * from customers''').fetchall())