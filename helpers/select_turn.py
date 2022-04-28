from  .control import ConectionDB

def SelectTurn(ident):
    sql = '''SELECT turnsID FROM turns WHERE Identification = '{}' and IsEnabled = 1 AND status = 'available' '''.format(ident)

    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row

  
        
    except Exception as e:
        print(e)
        return None
    
