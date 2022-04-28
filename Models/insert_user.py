from werkzeug.security import  generate_password_hash
from  helpers.control import ConectionDB

def InsertUser(username,password):
    """
    insert username and  password in users
    :param request:
    """
    sql = '''INSERT INTO Users(UserName,Password) VALUES ('{}','{}')'''.format(username,generate_password_hash(password))
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
        # return "El usuario no pudo ser registrado"
    finally:
        if conn:
            conn.close()
    


def insert_cashier_user(comp_select,username):
    query = """SELECT UserID from Users WHERE UserName = '{}'""".format(username)

    
    conn = ConectionDB()
    
    try:
        cur = conn.cursor()
        
        cur.execute(query)
        row = cur.fetchone()
  
        sql = '''INSERT INTO CashierUsers(CashierID,UserID) VALUES ('{}','{}')'''.format(comp_select,row[0])
   
        cur.execute(sql)
        conn.commit()

        return True 
    except Exception as e:
        print(e)
        return None
        # return "El usuario no pudo ser registrado"
    finally:
        if conn:
            conn.close()
  