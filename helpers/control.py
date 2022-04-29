import sqlite3 as sql

def ConectionDB():
    conn = None
    try:
        conn = sql.connect("db\System_turn.db",timeout=1)
    except Exception as e:
        print(e)

    return conn


def InsertAndUpdate(query_insert):
    conn = ConectionDB()
    try:
        cur = conn.cursor()
        cur.execute(query_insert)
        conn.commit() 
        return True

    except Exception as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()


def QuerySelectOne(query_Select):
    conn = ConectionDB()
    try:
        cur = conn.cursor()
        cur.execute(query_Select)
        row = cur.fetchone()
        return row

    except Exception as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()
    