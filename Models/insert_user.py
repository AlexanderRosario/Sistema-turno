from werkzeug.security import  generate_password_hash
from  helpers.control import InsertAndUpdate,QuerySelectOne

def InsertUser(username,password):
    """
    insert username and  password in users
    :param request:
    """
    sql = '''INSERT INTO Users(UserName,Password) VALUES ('{}','{}')'''.format(username,generate_password_hash(password))

    return InsertAndUpdate(sql) 




def insert_cashier_user(comp_select,username):
    query = """SELECT UserID from Users WHERE UserName = '{}'""".format(username)

    
    row = QuerySelectOne(query)
  
    sql = '''INSERT INTO CashierUsers(CashierID,UserID) VALUES ('{}','{}')'''.format(comp_select,row[0])
   
    return InsertAndUpdate(sql)
        