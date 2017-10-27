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



app = Flask(__name__)
app.config['SECRET_KEY'] = "un string muy dificil de adivinar"
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


        
class MiFormulario(FlaskForm):
    name = StringField('Usuario', validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Alta(FlaskForm):
    usuario = StringField('Usuario' , validators=[DataRequired()]) 
    password1 = StringField('Password',validators=[DataRequired()])
    password2 = StringField(' Validar Password',validators=[DataRequired()])
    submit = SubmitField('Validar')      
    
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
                    return render_template('fortinero.html')          
    return render_template('login.html', form=formulario)

@app.route('/',methods=['GET' , 'POST'])
def principal():
    return render_template('index.html' , fecha_actual=datetime.utcnow())

@app.route('/register',methods=['GET' , 'POST'])
def register():
    alta = Alta()
    if alta.validate_on_submit():
        if alta.password1.data == alta.password2.data:
            password = alta.password2.data
            nombre_archivo = 'csv'    
            with open(nombre_archivo , 'a') as archivo:
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow([alta.usuario.data , password])
                return redirect('/login')
        else:
            return "Revise la contraseña"               
    return render_template('register.html', form=alta)

@app.route('/usuarios',methods=['GET' , 'POST'])
def saludar():
    formulario = MiFormulario()
    if request.method == 'POST':
        name = request.form['name']
        return render_template('saludo.html',name=name)
    return render_template('usuarios.html' , form=formulario)

@app.route('/about',methods=['GET' , 'POST'])
def contacto():
    return render_template('about.html')

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()
