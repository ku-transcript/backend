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

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn