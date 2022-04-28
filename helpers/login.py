
from werkzeug.security import check_password_hash
from  .control import ConectionDB

def ValidateUser( request):
    """
    Select user and validate password
    :param conn:
    :param request:
    :return: project id
    """
    sql = '''SELECT UserID, UserName,Password FROM  Users WHERE UserName = '{}' '''.format(request.form['username'])

    conn = ConectionDB()
    
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        # print(row)
        if not row:
            return "Ususario no registrado"
            

        if check_password_hash(row[2],request.form['password']) != True:
            return "El Usuario o Contraseña no son correctas"

        dict_user = {"id":row[0],
                    "username":row[1]}


        return dict_user

        
    except Exception as e:
        print(e)
    
