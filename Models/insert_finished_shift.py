from  helpers.control import InsertAndUpdate

def InsertAttendedTurn(userid,num_turn,description):
    # sql = '''INSERT INTO FinishedShift (UserID,TurnsID,Description) VALUES ({},{},'{}')'''.format(userid,num_turn,description)
    #esto debe ser un update
    sql = '''UPDATE Turns SET  FinishedAt = DateTime('now'), Status = 'finished'
                    WHERE TurnsID = {0} AND UserID= {1}'''.format(num_turn,userid,description)

    return InsertAndUpdate(sql)
  