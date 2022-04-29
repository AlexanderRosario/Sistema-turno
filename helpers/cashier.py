from  .control import ConectionDB

def select_cashier():
    sql = '''SELECT CashierID,name FROM Cashiers WHERE IsEnabled = 1'''

    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        print(row)
        if not row:
            return "no hay cajas"
  
        return row

        
    except Exception as e:
        print(e)
    


