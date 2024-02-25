import sqlite3

connection = sqlite3.connect('courses.db')


with open('schema.sql', "rb") as f:
    connection.executescript(f.read().decode('utf8'))

connection.commit()
print("Initialized the database.")
connection.close()