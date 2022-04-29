from  helpers.control import InsertAndUpdate

def InsertAttendedTurn(userid,num_turn,description):
    # sql = '''INSERT INTO FinishedShift (UserID,TurnsID,Description) VALUES ({},{},'{}')'''.format(userid,num_turn,description)
    #esto debe ser un update
    sql = '''UPDATE FinishedShift SET Description='{2}',Status= 'Finished'
                    WHERE TurnsID = {1} AND UserID= {0} AND Description ='{2}' '''.format(userid,num_turn,description)
  
    return InsertAndUpdate(sql)
  