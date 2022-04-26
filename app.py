
from flask import Flask, render_template, request,redirect, url_for
from flask_cors import CORS
from config import config
from models.login import ValidateUser
from models.register import InsertUser

app = Flask(__name__)
CORS(app)



def initialize_app(config):
    app.config.from_object(config)
    return app

app = initialize_app(config['development'])
# mail = Mail(app)

@app.route('/menu',methods=['GET'])
def  menu():
    
    # for i in request.application.__code__:
    #     print(i)
    # if request.get_json() == 201:
    #     return render_template('layouts/index.html',message = "Usuario creado")
    return render_template('layouts/index.html') 

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
        return user
    return redirect(url_for('menu')) 







@app.route('/register',methods=['get'])
def singup():

    if  request.args.get('messaje') or  request.args.get('user'):
        return render_template('layouts/register.html',message=request.args.get('messaje'),user=request.args.get('user')),403
    return render_template('layouts/register.html')


@app.route('/register',methods=['POST'])
def PostRegister(): 
    
    if request.form['password'] != request.form['password-repeat']:
        return render_template('layouts/register.html',message='La Contraseña no coinciden')

    if not InsertUser(request):
        return render_template('layouts/register.html',user='No pudo ser creado')

    return render_template('layouts/register.html',success="Se ha creado el usuario")


@app.route('/cashier',methods=['GET'])
def cashier():
    print('hola')
    return request


@app.after_request
def log_the_status_code(response):
    # status_as_string = response.status
    # status_as_integer = response.status_code
    # logging.warning("status as string %s" % status_as_string)
    # logging.warning("status as integer %s" % status_as_integer)
    # print(response.status_code)
    return response

if __name__=='__main__':
    # app.debug(False)
    app.run(port=8000,debug=True)
