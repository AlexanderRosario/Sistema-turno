from telnetlib import PRAGMA_HEARTBEAT
from  .control import InsertAndUpdate,QuerySelectOne,SelectList

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

def SelectListTurn():
    sql = '''SELECT Cashiers.Name,FinishedShift.turnsID FROM FinishedShift 
	            INNER JOIN Users ON Users.UserID = FinishedShift .UserID
	            INNER JOIN CashierUsers on CashierUsers.UserID = users.UserID
	            INNER JOIN Cashiers on Cashiers.CashierID = CashierUsers.CashierID 
                    WHERE FinishedShift.IsEnabled = 1 AND status = 'attending'  '''

    return SelectList(sql)


def SelectInfoBusinness():
    
    sql = ''' SELECT ID,Logo,Name,address,Phone,email,UpdateAt from InfoBusiness; '''
    
    return QuerySelectOne(sql)


def UpdateInfoBusiness(id,name,address,phone,email):
    sql_update = '''UPDATE InfoBusiness SET   Name='{}',
                                                address ='{}',
                                                Phone='{}',
                                                email='{}',
                                                UpdateAt= datetime('now') WHERE ID = '{}' '''.format(name,address,phone,email,id

                                                )


    return InsertAndUpdate(sql_update)


def Updatecashier(id,name):
    sql_update = '''UPDATE Cashiers SET   Name='{}'
                                                WHERE CashierID = '{}' '''.format(name,id

                                                )
    print(sql_update)
    return InsertAndUpdate(sql_update)


def Deletecashier(id):
    sql_update = '''Delete FROM Cashiers WHERE CashierID = {} '''.format(id)
    print(sql_update)
    return InsertAndUpdate(sql_update)
