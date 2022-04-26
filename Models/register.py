from werkzeug.security import check_password_hash, generate_password_hash
from  .control import ConectionDB
from flask.json import jsonify

 

def InsertUser(request):
    """
    insert username and  password in users
    :param request:
    """
    sql = '''INSERT INTO Users(UserName,Password) VALUES ('{}','{}')'''.format(request.form['username'],generate_password_hash(request.form['password']))
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
    


