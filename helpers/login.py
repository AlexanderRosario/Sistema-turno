
from werkzeug.security import check_password_hash
from  .control import ConectionDB

def ValidateUser( request):
    """
    Select user and validate password
    :param conn:
    :param request:
    :return: project id
    """
    sql = '''SELECT UserID, UserName,Password,userRol FROM  Users WHERE UserName = '{}' AND IsEnabled = 1 '''.format(request.form['username'])
    # print(sql)
    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        # print(row)
        if not row:
            return "Ususario no registrado"
        # print(row[1])   

        if check_password_hash(row[2],request.form['password']) != True:
            return "El Usuario o Contraseña no son correctas"

        
        

        caja = SelectUserCashier(conn,row[0])
        # print(row)
        # print(caja)
        dict_user = {"id":row[0],
                    "username":row[1],
                    "rol":row[3],
                    "cashiername": caja[0]}
        return dict_user

        
    except Exception as e:
        print(e)
    
def SelectUserCashier(conn,id):
    sql = '''SELECT   Cashiers.Name from CashierUsers INNER join  Cashiers on Cashiers.CashierID = CashierUsers.CashierID where CashierUsers.UserID ={} AND CashierUsers.IsEnabled = 1'''.format(id)
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        rowcashier = cur.fetchone()
        print(rowcashier)
        if not rowcashier:
            return None
  
        return rowcashier

        
    except Exception as e:
        print(e)
    
