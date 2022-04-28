from  helpers.control import ConectionDB

def insertTurn(ident,description):
    sql = '''INSERT INTO turns (Identification,description) VALUES ('{}','{}')'''.format(ident,description)
    conn = ConectionDB()
    
    try:
        # print(sql)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()   
        return True  
    except Exception as e:
        print(e)
        return None
       
    finally:
        if conn:
            conn.close()
    