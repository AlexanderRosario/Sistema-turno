
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
    




# from helpers.Validation_token import write_token

        
#         if not user:
#             response = jsonify({"message":"No se ha encontrado este Usuario."})
#             response.status_code = 400

#             return response

#         if Users.password_verific(user[0][4],password):
            
#             user = serializerUser(user)
            
            
#             token = write_token(data = user)
            
#             response = jsonify({"user":user,
#                                 "token":token})
#             response.status_code = 200
            
            
#             return  response

#         else:
#             response = jsonify({"message": "El email o la contraseña no coinciden."})
#             response.status_code = 404
#             return response
#     except Exception as e:

#         print(e)


# def serializerUser(users):

#     info_user = {
#         "Id": users[0][0],
#                 "Name":users[0][1]
#                 ,"Lastname":users[0][2]
#                 ,"email":users[0][3]
#                 }

    
    

#     return info_user


        


    





