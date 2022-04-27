from werkzeug.security import  generate_password_hash
from  helpers.control import ConectionDB


 

def InsertUser(request):
    """
    insert username and  password in users
    :param request:
    """
    sql = '''INSERT INTO Users(UserName,Password) VALUES ('{}','{}')'''.format(request.form['username'],generate_password_hash(request.form['password']))
    conn = ConectionDB()
    print(request.form['comp_select'])
    try:
        # print(sql)
        
        # cur = conn.cursor()
        # cur.execute(sql)
        # conn.commit()   
        return True  
    except Exception as e:
        print(e)
        return None
        # return "El usuario no pudo ser registrado"
    finally:
        if conn:
            conn.close()
    


def insert_cashier_user(request):
    query = """SELECT UserID from Users WHERE UserName = {}""".form(request.form['Username'])

    sql = '''INSERT INTO CashierUsers(CashierID,UserID) VALUES ('{}','{}')'''.format(request.form['comp_select'])
    conn = ConectionDB()
    
    try:
        # print(sql)
        
        # cur = conn.cursor()
        # cur.execute(sql)
        # conn.commit()   
        return True  
    except Exception as e:
        print(e)
        return None
        # return "El usuario no pudo ser registrado"
    finally:
        if conn:
            conn.close()
    
