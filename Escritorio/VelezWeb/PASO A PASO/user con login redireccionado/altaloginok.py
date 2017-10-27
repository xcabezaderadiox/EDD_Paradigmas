from flask import Flask , render_template , session , request , redirect , url_for ,flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
import csv
app = Flask(__name__)
app.config['SECRET_KEY'] = "un string muy dificil de adivinar"



        
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
                    return redirect('/')
                    
    return render_template('login.html', form=formulario)

@app.route('/',methods=['GET' , 'POST'])
def principal():
    flash("Bienvenido!!")
    return render_template('principal.html')

@app.route('/register',methods=['GET' , 'POST'])
def login2():
    flash("Cree su usuario")
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



if __name__ == "__main__":
    app.run(debug=True)
