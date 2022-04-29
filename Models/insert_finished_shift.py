from  helpers.control import ConectionDB

def InsertAttendedTurn(userid,num_turn,description):
    # sql = '''INSERT INTO FinishedShift (UserID,TurnsID,Description) VALUES ({},{},'{}')'''.format(userid,num_turn,description)
    sql = '''INSERT INTO FinishedShift(UserID,TurnsID,Description)  
                SELECT {0}, {1},'{2}'
                    WHERE NOT EXISTS(SELECT 1 FROM FinishedShift WHERE TurnsID = {1} AND UserID= {0} AND Description ='{2}')'''.format(userid,num_turn,description)
    print(sql)
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
    
