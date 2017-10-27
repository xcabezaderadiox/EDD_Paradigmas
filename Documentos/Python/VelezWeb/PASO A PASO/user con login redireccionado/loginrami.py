import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class Formulario_Logueo(FlaskForm):
    name = StringField('Ingrese Usuario', validators=[DataRequired()])
    password = StringField('Ingrese contraseña', validators=[DataRequired()])

class Formulario_Registro(FlaskForm):
    name = StringField('Ingrese Usuario', validators=[DataRequired()])
    password1 = StringField('Ingrese Contraseña', validators=[DataRequired()])
    password2 = StringField('Ingrese Contraseña nuevamente', validators=[DataRequired()])

app.config['SECRET_KEY'] = 'un string que funcione como llave'

@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_logueo = Formulario_Logueo()
    if form_logueo.validate_on_submit():
        with open("usuarios", "r") as archivo:
            f = csv.reader(archivo)
            for linea in f:
                p = linea
                a = p[0]
                b = p[1]
                if form_logueo.name.data == a and form_logueo.password.data == b:
                    return "Logueado"
    return render_template('login.html', form=form_logueo)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form_registro = Formulario_Registro()
    if form_registro.validate_on_submit():
        if form_registro.password1.data == form_registro.password2.data:
            with open('usuarios', 'a') as archivo:
                f = csv.writer(archivo)
                f.writerow([form_registro.name.data, form_registro.password1.data])
        else:
            return "Revise la contraseña"
    return render_template('register.html', form=form_registro)

@app.route('/usuarios')
def saludar(usuario):
    return render_template('usuarios.html', nombre=usuario)

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()

