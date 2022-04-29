from  .control import ConectionDB

def SelectNewTurn(ident):
    sql = '''SELECT turnsID FROM turns WHERE Identification = '{}' AND IsEnabled = 1 AND status = 'available'  AND CreatedAt=(SELECT MAX(CreatedAt) FROM turns) '''.format(ident)

    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row

  
        
    except Exception as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()
    

def SelectShift():
    # sql = '''SELECT turnsID FROM turns WHERE IsEnabled = 1 AND status = 'available'  AND CreatedAt=(SELECT MIN(CreatedAt) FROM turns) '''
    sql= '''WITH  available as (SELECT turnsID,CreatedAt FROM turns WHERE IsEnabled = 1 AND status = 'available')
                SELECT * from available WHERE CreatedAt=( select MIN(CreatedAt) from available)'''

    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()

        sql = '''UPDATE turns SET  status = 'attending' , UpdateAt=DateTime('now') WHERE turnsID = '{}' '''.format(row[0])
        cur.execute(sql)
        conn.commit() 

        return row
        

  
        
    except Exception as e:
        print(e)
        return None


    finally:
        if conn:
            conn.close()
    