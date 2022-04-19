
from  .control import ConectionDB


def ValidateUser(conn, request):
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
        if row:
            if request.form['password'] == row[2]:
                return row
            return "El Usuario o Contraseña no son correctas"

        return "Ususario no registrado"
    except Exception as e:
        print(e)
    
    





