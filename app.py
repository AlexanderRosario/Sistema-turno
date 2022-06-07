from flask import Flask, render_template, request,redirect, url_for
from flask_cors import CORS
from config import config
from helpers.login import ValidateUser
from models.insert_user import InsertUser , insert_cashier_user
from models.insert_cashier import InsertCashier
from models.insert_turn import insertTurn
from models.insert_finished_shift import InsertAttendedTurn
from helpers.cashier import select_cashier
from helpers.select_turn import (SelectNewTurn,SelectShift,SelectListTurn,SelectInfoBusinness,
UpdateInfoBusiness,Updatecashier,Deletecashier,SelectUsers,UpdateUser,DeleteUserSql,Services,Truncate_table,
reset_table)
from helpers.ticket_pdf import generate_pdf
app = Flask(__name__)
CORS(app)



def initialize_app(config):

    app.config.from_object(config)

    return app

app = initialize_app(config['development'])
# mail = Mail(app)

@app.route('/menu',methods=['GET'])
def  menu():
    return render_template('layouts/menu.html')

@app.route('/')
def Index():
    return render_template('layouts/login.html')
    

@app.route('/login',methods=['GET'])
def Login():
    return render_template('layouts/login.html')

@app.route('/login',methods=['POST'])
def PostLogin():
    user = ValidateUser(request)
    if type(user) != dict:

        return render_template('layouts/login.html',error='No se encuentra el usuario.')

    if user["rol"] =="admin":
        return redirect(url_for('menu')) 

    if user["rol"] == "cajero":
        # dict_user = {"id":row[0],
        #             "username":row[1],
        #             "rol":row[3],
        #             "cashiername": caja[0]}
        
        return redirect(url_for(endpoint='CashierService',cashiername=user["cashiername"],username=user["username"],userid=user['id']))
    return render_template('layouts/login.html')



@app.route('/register',methods=['GET'])
def singup():
    if  request.args.get('messaje') or  request.args.get('user'):

        return render_template('layouts/register.html',message=request.args.get('messaje'),user=request.args.get('user')),403
    return render_template('layouts/register.html',data=select_cashier())



@app.route('/register',methods=['POST'])
def PostRegister(): 

    if request.form['password'] != request.form['password-repeat']:
        return render_template('layouts/register.html',message='La Contraseña no coinciden',data=select_cashier())

    if not InsertUser(request.form['username'].lower(),request.form['password']):
        return render_template('layouts/register.html',user='No pudo ser creado',data=select_cashier())
        
    if not insert_cashier_user(request.form['comp_select'],request.form['username']):
        return render_template('layouts/register.html',user='No pudo ser asignado a una caja',data=select_cashier())
    return render_template('layouts/register.html',success="Se ha creado el usuario",data=select_cashier())



@app.route('/cashier',methods=['GET'])
def cashier():
    return render_template('layouts/cashier.html')



@app.route('/cashier',methods=['POST'])
def cashier_post():

    if   not request.form['namecashier']:
        return render_template('layouts/cashier.html',error ="Se debe llenar el campo")

    if InsertCashier(request.form['namecashier'])!= True:
        return render_template('layouts/cashier.html',error ="Se ha producido un error")
    return render_template('layouts/cashier.html',messaje = "Se ha creado la caja")



@app.route('/turn',methods=['GET'])
def turn():
    return render_template('layouts/turn.html',services=Services())



@app.route('/turn',methods=['POST'])
def turn_post():
    services = Services()

    if not request.form['ident']:
        return render_template('layouts/turn.html',error = "Debe llenar la casilla de la Identificacion.",services=services)

    if insertTurn(request.form['ident'],request.form['description']) != True:

        return render_template('layouts/turn.html',error = "No se pudo generar el turno.",services=services)
        # return redirect(url_for('selectnewturn',ident =request.form['ident']))

    num_turn = SelectNewTurn(request.form['ident'])
    if not num_turn:
        return render_template( 'layouts/viewturn.html' ,error = "No hay turnos disponibles",services=services)
    print(num_turn)
    if generate_pdf(num_turn[0],request.form['description']) != True:
        return render_template('layouts/turn.html',error = "No se pudo generar el ticket",services=services)
    return render_template('layouts/viewturn.html',success = "Se ha gerado el PDF" , num_turn = num_turn[0])
    #     render_template('layouts/viewturn.html',error = "Debe llenar la casilla de la Identificacion.")



@app.route('/service',methods=['GET'])
def CashierService():

    if not request.args.get("cashiername"):
        return redirect(url_for('Login'))

    
    num_turn = SelectShift(request.args.get("userid"))
    if not num_turn:
        # no puedo encontrar un turno nuevo 
        return render_template('layouts/cashier_service.html',cashiername=request.args.get("cashiername"),username = request.args.get("username"),userid=request.args.get("userid"),num_turn=None,error="No hay turnos disponible, espera uno..." )

    return render_template('layouts/cashier_service.html',cashiername=request.args.get("cashiername"),username = request.args.get("username"),userid=request.args.get("userid"),num_turn=num_turn[0])


@app.route('/service',methods=['POST'])
def NextTurn():
   
    if InsertAttendedTurn(request.form['userid'],request.form['num_turn'],request.form['description']) != True:
        # no se pudo finalizar la transacion
        return render_template('layouts/cashier_service.html',cashiername = request.form.get('cashiername'),username=request.form.get('username'),userid=request.form.get("userid"),num_turn=0,error="ya existe este registro intenta cerrar y abrir sesion" )
   
    num_turn = SelectShift(request.form['userid'])

    if not num_turn:
        # no puedo encontrar un tur no nuevo 
        return render_template('layouts/cashier_service.html',cashiername= request.form.get('cashiername'),username=request.form.get('username'),userid=request.form.get("userid"),num_turn=None,error="No hay turnos disponible, espera uno..." )
    return render_template('layouts/cashier_service.html',cashiername= request.form.get('cashiername'),username=request.form.get('username'),userid=request.form.get("userid"),num_turn= num_turn[0])



@app.route('/listurn',methods=['GET'])
def ViewListTurn():
    return render_template('layouts/list_turn.html',data=SelectListTurn())



@app.route('/infbusiness',methods=['GET'])
def InfoBusiness():

    Info_Business = SelectInfoBusinness()

    if not Info_Business:
        return render_template('layouts/info_business.html',error="No hay Informacion registrada" )

    return render_template('layouts/info_business.html',data=Info_Business)



# @app.route('/get_ip', methods=['GET'])
# def get_tasks():
#     if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#         return {'ip': request.environ['REMOTE_ADDR']}, 200
#     else:
#         return {'ip': request.environ['HTTP_X_FORWARDED_FOR']}, 200




@app.route('/editinfbusiness',methods=['GET','POST'])
def EditInfoBusiness():

    Info_Business = SelectInfoBusinness()

    if request.method == 'GET':
        if not Info_Business:
             return render_template('layouts/cashier_service.html',error="No hay turnos disponible espera uno" )
             
        return render_template('layouts/edit_info_business.html',data=Info_Business)
        
    elif request.method == 'POST':

        if UpdateInfoBusiness(request.form['id'],request.form['name'],request.form['addres'],request.form['phone'],request.form['email']):
        
            return redirect(url_for('InfoBusiness'))
        return redirect(url_for('InfoBusiness')) 



@app.route('/editcashier',methods=['GET','POST'])
def EditCashier():
    if request.method == 'GET':
        return render_template('layouts/edit_cashier.html',data=select_cashier())

    elif request.method == 'POST':
        if   not request.form['id_caja'] or  not request.form['name']:
            return render_template('layouts/edit_cashier.html',error ="Se deben completar los campo",data=select_cashier())
        
        if Updatecashier(request.form['id_caja'],request.form['name']):


            return render_template('layouts/edit_cashier.html',update="Actualizado la caja",data=select_cashier())

        return redirect(url_for('EditCashier'),update="No se pudo modificar",data=select_cashier()) 



@app.route('/deletecashier',methods=['GET','POST'])
def deletCashier():
    if request.method == 'GET':
        return render_template('layouts/delete_cashier.html',data=select_cashier())

    elif request.method == 'POST':
        if   not request.form['id_caja']:
            return render_template('layouts/delete_cashier.html',error ="Deben Selecionar un campo",data=select_cashier())

        if Deletecashier(request.form['id_caja']):
            return render_template('layouts/delete_cashier.html',deleted="Se ha Eliminado la caja",data=select_cashier())

        return render_template ('layouts/delete_cashier.html',error="No se puedo Eliminar",data=select_cashier())



@app.route('/editUser',methods=['GET','POST'])
def EditUser():
    if request.method == 'GET':
        return render_template('layouts/edit_user.html',cajas = select_cashier(),users=SelectUsers())

    elif request.method == 'POST':
        if not request.form['name']:
            return render_template('layouts/edit_user.html',error="No deje ningun campo vacio",cajas=select_cashier()) 
        
        if UpdateUser(request.form['id_user'],request.form['name'],request.form['id_caja'])!= True:
            return  render_template('layouts/edit_user.html',error="No se puedo modificar",cajas=select_cashier()) 


        return render_template('layouts/edit_user.html',update="Se actualizo el usuario",cajas=select_cashier(),users=SelectUsers())

        


@app.route('/deleteUser',methods=['GET','POST'])
def DeleteUser():
    if request.method == 'GET':
        return render_template('layouts/delete_user.html' ,users = SelectUsers())

    elif request.method == 'POST':
        if not request.form['id_user']:
            return render_template('layouts/delete_user.html' ,error = "No deje ningun campo vacio" ,cajas = select_cashier()) 
        
        if DeleteUserSql(request.form['id_user'])!= True:
            return  render_template('layouts/delete_user.html' ,error = "No se puedo Eliminar" ,cajas = select_cashier())

        return render_template('layouts/delete_user.html' ,deleted = "Se elimino el usuario" ,users = SelectUsers())



@app.route('/reset',methods=['GET'])
def Reset():
    if Truncate_table() != True:
        return redirect(url_for('menu'))
    if reset_table() != True:
        return redirect(url_for('menu'))
    return render_template('layouts/menu.html', success = " Se reiniciaron los turnos.")






@app.route('/heatmap',methods=['GET'])
def HeatMap():
    # value = df_frame()
    # if value['is_success']:
    return render_template('layouts/heatmap.html') 
    # return "Error con la visual"


@app.after_request
def log_the_status_code(response):
    # print(response.status)
    # print( response.status_code)
    # # logging.warning("status as string %s" % status_as_string)
    # # logging.warning("status as integer %s" % status_as_integer)
    # print(response.status_code)
    # cors_after_request(app.make_response(f(*args, **kwargs)))
    return response



if __name__=='__main__':
    # app.debug(False)
    app.run(port=8000,host= '0.0.0.0')

