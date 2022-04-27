from  helpers.control import ConectionDB

def InsertCashier(cashier_name):
    sql = '''INSERT INTO Cashiers (name) VALUES ('{}')'''.format(cashier_name)
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
    

