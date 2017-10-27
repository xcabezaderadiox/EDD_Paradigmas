from flask import Flask , render_template , session , request , redirect , url_for ,flash 
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import csv
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
import pandas as pd
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = "un string muy dificil de adivinar"
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

lista = []
nombre_archivo = 'csv'    
with open(nombre_archivo) as archivo:
    archivo_csv = csv.reader(archivo)  
    for linea in archivo_csv:
        valores = linea
        a = valores[0]
        lista.append(a)
   
class MiFormulario(FlaskForm):
    name = StringField('Usuario', validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Alta(FlaskForm):
    usuario = StringField('Usuario' , validators=[DataRequired()]) 
    password1 = StringField('Password',validators=[DataRequired()])
    password2 = StringField(' Validar Password',validators=[DataRequired()])
    submit = SubmitField('Validar')      
    
class Consulta(FlaskForm):
    cancha = StringField('Cancha')
    equipo = StringField('Equipo')
    fecha = StringField('Fecha')



@app.route('/login',methods=['GET' , 'POST'])
def login():
    formulario = MiFormulario()
    if formulario.validate_on_submit():
        nombre_archivo = 'csv'    
        with open(nombre_archivo) as archivo:
            archivo_csv = csv.reader(archivo)
            for linea in archivo_csv:
                valores = linea
                a = valores[0]
                b = valores[1]
                if a == formulario.name.data and b == formulario.password.data:
                    session['username'] = formulario.name.data 
                    return render_template('fortinero.html')             
    return render_template('login.html', form=formulario,username=session.get('username'))

@app.route('/',methods=['GET' , 'POST'])
def principal():
    if 'username' in session:
        return render_template('index.html', fecha_actual=datetime.utcnow())
    return render_template('loguearte.html')

@app.route('/register',methods=['GET' , 'POST'])
def register():
    alta = Alta()
    if alta.validate_on_submit():
        if alta.usuario.data not in lista:
            if alta.password1.data == alta.password2.data:
                password = alta.password2.data
                nombre_archivo = "csv"
                with open(nombre_archivo , 'a') as archivo:
                    archivo_csv = csv.writer(archivo)
                    archivo_csv.writerow([alta.usuario.data , password])
                    return redirect('/login')
            else:
                return render_template('credenciales.html')  
        else:
            return render_template('usuariorepetido.html')                
    return render_template('register.html', form=alta)

@app.route('/usuarios',methods=['GET' , 'POST'])
def saludar():
    formulario = MiFormulario()
    if request.method == 'POST':
        name = request.form['name']
        return render_template('saludo.html',name=name)
    return render_template('usuarios.html' , form=formulario)

@app.route('/fixture',methods=['GET' , 'POST'])
def lerr():
    nombre_archivo = 'csv2' 
    with open(nombre_archivo) as archivo:
        commentList = csv.reader(archivo)
        return render_template('tabla.html',commentList=commentList)

@app.route('/filtro/cancha',methods=['GET' , 'POST'])
def filtro():
    with open('cancha', 'w') as archivo:
        archivo.truncate()
    consulta = Consulta()
    df = pd.read_csv('csv2')
    if consulta.validate_on_submit():
        df2 = df[df['CANCHA'] == consulta.cancha.data]
        df3 = df2.to_csv('cancha' ,index=None )
        with open('cancha') as archivo:
            canchas = csv.reader(archivo)
            cabeza = next(canchas)
            return render_template('cancha.html',cabeza=cabeza,canchas=canchas)
    return render_template('filtro.html' , consulta=consulta)

@app.route('/filtro/equipo',methods=['GET' , 'POST'])
def equipo():
    with open('equipo', 'w') as archivo:
        archivo.truncate()
    consulta_equipo = Consulta()
    df4 = pd.read_csv('csv2')
    if consulta_equipo.validate_on_submit():
        df5 = df4[df4['EQUIPO'] == consulta_equipo.equipo.data]
        df6 = df5.to_csv('equipo' ,index=None )
        with open('equipo') as archivo:
            resultado = csv.reader(archivo)
            encabezado = next(resultado)
            return render_template('equipo.html',encabezado=encabezado,resultado=resultado)
    return render_template('filtro.html' , consulta_equipo=consulta_equipo)

@app.route('/filtro/fecha',methods=['GET' , 'POST'])
def fecha():
    with open('fecha', 'w') as archivo:
        archivo.truncate()
    consulta_fecha = Consulta()
    df7 = pd.read_csv('csv2')
    if consulta_fecha.validate_on_submit():
        df8 = df7[df7['FECHA'] == consulta_fecha.fecha.data]
        df9 = df8.to_csv('fecha' ,index=None )
        with open('fecha') as archivo:
            date = csv.reader(archivo)
            head = next(date)
            return render_template('fecha.html',head=head,date=date)
    return render_template('filtro.html' , consulta_fecha=consulta_fecha)

@app.route('/about',methods=['GET' , 'POST'])
def contacto():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()
