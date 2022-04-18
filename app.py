from flask import Flask, render_template, request
from flask_cors import CORS
from config import config
import datetime

app = Flask(__name__)
CORS(app)



def initialize_app(config):
    app.config.from_object(config)
    return app

app = initialize_app(config['development'])
# mail = Mail(app)


@app.route('/')
def Index():
    return render_template('layouts/index.html', utc_dt=datetime.datetime.utcnow())
    

@app.route('/login',methods=['GET'])
def Login():
    return render_template('layouts/login.html')

@app.route('/login',methods=['POST'])
def PostLogin():
    print(request.form['uname'])
    return "recibido"



if __name__=='__main__':
    app.run(port=8000)
