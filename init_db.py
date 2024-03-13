import sqlite3 

from flask import g

#path to database SQLite
DATABASE = 'database.db'

#Initializes the database.db, if not exist, it will be created.
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        with open('schema.sql', 'r') as f:
            schema = f.read()
        conn.executescript(schema)
    print("Database initialized successfully.")

#Connexion to database
def get_db():   
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#Close connexion to database
def close_db():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

