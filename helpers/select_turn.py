from  .control import InsertAndUpdate,QuerySelectOne

def SelectNewTurn(ident):
    sql = '''SELECT turnsID FROM turns WHERE Identification = '{}' AND IsEnabled = 1 AND status = 'available'  AND CreatedAt=(SELECT MAX(CreatedAt) FROM turns) '''.format(ident)
    return QuerySelectOne(sql)
    

def SelectShift(userid):
    # sql = '''SELECT turnsID FROM turns WHERE IsEnabled = 1 AND status = 'available'  AND CreatedAt=(SELECT MIN(CreatedAt) FROM turns) '''
    sql= '''WITH  available as (SELECT turnsID,CreatedAt FROM turns WHERE IsEnabled = 1 AND status = 'available')
                SELECT * from available WHERE CreatedAt = ( select MIN(CreatedAt) from available) '''
    row = QuerySelectOne(sql)
    if not row:
        return row

    query_for_view_windows = '''INSERT INTO FinishedShift(UserID,TurnsID,Status)  
               SELECT {0}, {1},'attending'
                    WHERE NOT EXISTS(SELECT 1 FROM FinishedShift WHERE TurnsID = {1} AND UserID= {0} )'''.format(userid,row[0])

    valid = InsertAndUpdate(query_for_view_windows) 
    if valid !=True :
        return valid

    
    sql_update = '''UPDATE turns SET  status = 'attending' , UpdateAt=DateTime('now') WHERE turnsID = '{}' '''.format(row[0])
    valid = InsertAndUpdate(sql_update)
    if valid != True:
        return  valid

    return row