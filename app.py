from flask import Flask, render_template, request, redirect, flash, session, send_from_directory
import os
from flaskext.mysql import MySQL
from datetime import timedelta, datetime
from random import randint
from consultaCedula import ConsultaAnonima

programa = Flask(__name__)
programa.secret_key = str(randint(10000, 99999))
programa.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST'] = '10.206.80.200'
programa.config['MYSQL_DATABASE_PORT'] = 3306
programa.config['MYSQL_DATABASE_USER'] = 'root'
programa.config['MYSQL_DATABASE_PASSWORD'] = ''
programa.config['MYSQL_DATABASE_DB'] = 'carreras'
mysql.init_app(programa)

conexion = mysql.connect()
cursor = conexion.cursor()

consultaA = ConsultaAnonima(mysql)

@programa.route('/')
def index():
    return render_template("consultaCedula.html")


@programa.route('/consultarCedula', methods = ['POST'])
def consultaCedula():
    cedula = request.form.get('cedula')

    if not consultaA.consulta(cedula):
        print('No se encontro en clientes')
        return render_template("registro.html")
    else:
        print("El cliente fue encontrado")
        return redirect("/")   
    
      






if __name__ == '__main__':
    programa.run(host='0.0.0.0', debug=True, port='8080')