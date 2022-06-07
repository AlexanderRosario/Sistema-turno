
from  .control import InsertAndUpdate,QuerySelectOne,SelectList

def SelectNewTurn(ident):
    sql = '''SELECT turnsID FROM turns WHERE IdentificationClient = '{}' AND IsEnabled = 1 AND status = 'available'  AND AvailableAt=(SELECT MAX(AvailableAt) FROM turns) '''.format(ident)
    
    return QuerySelectOne(sql)
    

def SelectShift(userid):
    # sql = '''SELECT turnsID FROM turns WHERE IsEnabled = 1 AND status = 'available'  AND CreatedAt=(SELECT MIN(CreatedAt) FROM turns) '''
    sql= '''WITH  available as (SELECT turnsID,AvailableAt FROM Turns WHERE IsEnabled = 1 AND Status = 'available')
                SELECT * from available WHERE AvailableAt = ( select MIN(AvailableAt) from available) '''
    row = QuerySelectOne(sql)


    if not row:
        return row
    if turns_is_attending(userid,row[0]):
        return row

def turns_is_attending(userid,turnsid):
    query_for_view_windows = '''UPDATE Turns SET UserID = {0}, status = 'attending',AttendedAt = DateTime('now') 
                    WHERE TurnsID = {1} '''.format(userid,turnsid)
    valid = InsertAndUpdate(query_for_view_windows) 

    if valid !=True :
        return valid

    return True
    # sql_update = '''UPDATE Turns SET  status = 'attending' , AttendedAt = DateTime('now') WHERE turnsID = '{}' '''.format(row[0])
    # valid = InsertAndUpdate(sql_update)
    # if valid != True:
    #     return  valid
    # return row



def SelectListTurn():
    sql = '''SELECT Cashiers.Name,Turns.turnsID FROM Turns
	            INNER JOIN Users ON Users.UserID = Turns.UserID
	            INNER JOIN CashierUsers on CashierUsers.UserID = users.UserID
	            INNER JOIN Cashiers on Cashiers.CashierID = CashierUsers.CashierID 
                    WHERE Turns.IsEnabled = 1 AND status = 'attending' ORDER BY Turns.turnsID desc '''

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
  
    return InsertAndUpdate(sql_update)


def Deletecashier(id):
    sql_update = '''update Cashiers set Isenabled = 0 WHERE CashierID = {} '''.format(id)

    return InsertAndUpdate(sql_update)

def SelectUsers():
    
    sql = ''' SELECT UserID,UserName,UserRol from Users 
                                                          Where IsEnabled = 1 and   UserRol = 'cajero'; '''
    
    return SelectList(sql)


def UpdateUser(id_user,username,id_caja):
    
    sql_update = '''UPDATE users SET  UserName='{1}'
                                                WHERE UserID = '{0}' AND IsEnabled = 1'''.format(id_user,username.lower())
    
 
    valid = InsertAndUpdate(sql_update)
    if valid !=True :
        return valid

    sql_update = '''UPDATE CashierUsers SET  CashierID = {0}  WHERE UserID = '{1}' AND IsEnabled = 1 '''.format(id_caja,id_user)
   
    return  InsertAndUpdate(sql_update)
   

def DeleteUserSql(id_user):
    sql_update = '''UPDATE users SET  IsEnabled=0
                                                WHERE UserID = '{0}' AND IsEnabled = 1'''.format(id_user)
  
    return  InsertAndUpdate(sql_update)


def Services():
    sql = ''' SELECT ServiceID,ServiceName FROM Services WHERE IsEnabled = 1;'''
    
    return SelectList(sql)

def Truncate_table():
    sql = '''DELETE from Turns;'''
    
    return InsertAndUpdate(sql)

def reset_table():
    sql = '''DELETE FROM sqlite_sequence WHERE name = 'Turns' ;'''
    
    return InsertAndUpdate(sql)