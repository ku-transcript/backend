# import sqlite3
# import os
# import click
# from flask import current_app, g
# from flask.cli import with_appcontext

# from data_source_file import DataSourceFile

# def get_db():
#     if 'db' not in g:
#         print(os.environ.get('DATABASE_URL'))
#         g.db = sqlite3.connect(
#             # os.environ.get('DATABASE_URL')
#           "./courses.db"
#             # detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         print("Connected")
#         g.db.row_factory = sqlite3.Row

#     return g.db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()
        
# def init_db():
#     db = get_db().cursor()
    
#     with current_app.open_resource('schema.sql') as f:
#         print(f.read().decode('utf8'))
#         db.executescript(f.read().decode('utf8'))

import sqlite3

connection = sqlite3.connect('courses.db')


with open('schema.sql', "rb") as f:
    connection.executescript(f.read().decode('utf8'))

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
print("Initialized the database.")
connection.close()