import sqlite3 as sql

def ConectionDB():
    conn = None
    try:
        conn = sql.connect("db\System_turn.db")
    except Exception as e:
        print(e)

    return conn
