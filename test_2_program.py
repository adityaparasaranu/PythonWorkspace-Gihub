import sqlite3

connection = sqlite3.connect('jose-udemy_projects/flask_restful-section_5/data.db')
cursor = connection.cursor()

# Creates a table names users
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "bob", "asdf")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, "aditya", "password"),
    (3, "aravind", "xyz")
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
print(list(cursor.execute(select_query)))
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()