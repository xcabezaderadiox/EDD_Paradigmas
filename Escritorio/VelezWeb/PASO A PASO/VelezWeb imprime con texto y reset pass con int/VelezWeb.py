#PRIMER BLOQUE DONDE SE IMPORTAN TODAS LAS FUNCIONALIDADES NECESARIAS
from flask import Flask , render_template , session , request , redirect ,flash ,send_file
from flask_wtf import FlaskForm
from wtforms import StringField ,IntegerField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import csv
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
import pandas as pd
import operator


app = Flask(__name__)
app.config['SECRET_KEY'] = "un string muy dificil de adivinar"
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

#ACA LO QUE HICE FUE CREAR UNA LISTA DONDE CADA VEZ QUE SE INICIA EL PROGRAMA SE CARGAN LOS USUARIOS EXISTENTES ASI SE VALIDA QUE NO SE CREE OTRO IGUAL
lista = []
nombre_archivo = 'csv'
with open(nombre_archivo) as archivo:
    archivo_csv = csv.reader(archivo)
    for linea in archivo_csv:
        valores = linea
        a = valores[0]
        b = valores[1]
        lista.append(a)
        lista.append(b)

#CLASES CREADAS PARA VALIDACION DE DATOS Y SOLICITUD DE FILTROS
class MiFormulario(FlaskForm):
    name = StringField('Usuario', validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Alta(FlaskForm):
    usuario = StringField('Usuario' , validators=[DataRequired()])
    password1 = StringField('Password',validators=[DataRequired()])
    password2 = StringField(' Validar Password',validators=[DataRequired()])
    submit = SubmitField('Validar')

class Reset(FlaskForm):
    old = StringField('Password antigua',validators=[DataRequired()])
    new = StringField('Nueva Password',validators=[DataRequired()])
    submit = SubmitField('Validar')

class Consulta(FlaskForm):
    cancha = StringField('Cancha')
    equipo = StringField('Equipo')
    fecha = StringField('Fecha')
    goles = IntegerField('Goles')

#AQUI COMIENZA EL BLOQUE CON LOS APPROUTE,TRATE DE ORDENALOS CRONOLOGICAMENTE A COMO LOS FUI HACIENDO Y COMO SE ESTRUTURAN EN LA WEB
@app.route('/index',methods=['GET' , 'POST'])
def principal():
    if 'username' in session:
        return render_template('index.html', fecha_actual=datetime.utcnow())
    return render_template('loguearte.html')


#LOGUEO DE USER
@app.route('/',methods=['GET' , 'POST'])
def login():
    formulario = MiFormulario()
    if formulario.validate_on_submit():
        nombre_archivo = 'csv'
        with open(nombre_archivo) as archivo:
            archivo_csv = csv.reader(archivo)
            log = next(archivo_csv)
            while log:
                if formulario.name.data == log[0] and formulario.password.data == log[1]:
                    session['username'] = formulario.name.data
                    session['password'] = formulario.password.data
                    return render_template('fortinero.html')
                log = next(archivo_csv,None)
            else:
                flash('Ingreso invalido,verifique sus credenciales')
                return redirect('/')
    return render_template('login.html', form=formulario)

#REGISTRO DEL USER
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
                    return redirect('/')
            else:
                return render_template('credenciales.html')
        else:
            return render_template('usuariorepetido.html')
    return render_template('register.html', form=alta)

#FUNCION PARA RESET DE PASSWORD
@app.route('/reset', methods=['GET', 'POST'])
def reset():   
    reset = Reset()
    passactual = session.get('password')
    useractual = session.get('username')
    if reset.validate_on_submit():
        if reset.old.data != passactual:
            flash('Revise su contraseña actual,sino registrese')
            return redirect('/reset')
        else:
            df = pd.read_csv('csv')
            df.loc[df.PASSWORD == int(passactual)] = useractual, reset.new.data
            df.to_csv('csv', index=None)
            flash('Modifico su contraseña')
            return redirect('/reset')
    return render_template('reset.html', form=reset)
    

#SALUDO AL NOMBRE DE USUARIO INGRESADO
@app.route('/usuarios',methods=['GET' , 'POST'])
def saludar():
    if 'username' in session:
        formulario = MiFormulario()
        if request.method == 'POST':
           name = request.form['name']
           return render_template('saludo.html',name=name)
        return render_template('usuarios.html' , form=formulario)
    return render_template('loguearte.html')

#IMPRESION DE TABLA,EN ESTE CASO UN FIXTURE DE UN TORNEO CON 3 COLUMNAS;EQUIPO,CANCHA Y FECHA
@app.route('/fixture',methods=['GET' , 'POST'])
def fixture():
    if 'username' in session:
        nombre_archivo = 'fixture'
        try:
            with open(nombre_archivo) as archivo:
                commentList = csv.reader(archivo)
                return render_template('tabla.html',commentList=commentList)
        except FileNotFoundError:
            return 'No se encuentra el archivo csv'
    return render_template('loguearte.html')


#FILTRO PARA CANCHAS
@app.route('/filtro/cancha',methods=['GET' , 'POST'])
def filtro():
    if 'username' in session:
        try:
            with open('cancha', 'w') as archivo:
                archivo.truncate()
        except FileNotFoundError:
            return 'No se encuentra el archivo'
        consulta = Consulta()
        df = pd.read_csv('fixture')
        if consulta.validate_on_submit():
           if consulta.cancha.data is "":
               return render_template('nulo.html')
           else:
               df2 = df[(df['CANCHA'].str.contains(consulta.cancha.data))]
               df3 = df2.to_csv('cancha' ,index=None )
               if df2.empty is True:
                   flash('No existe esa cancha')
                   return redirect('/filtro/cancha')
               else:
                   with open('cancha') as archivo:
                       canchas = csv.reader(archivo)
                       cabeza = next(canchas)
                       return render_template('cancha.html',cabeza=cabeza,canchas=canchas)
        return render_template('filtro.html' , consulta=consulta)
    return render_template('loguearte.html')

#FILTRO PARA EQUIPOS
@app.route('/filtro/equipo',methods=['GET' , 'POST'])
def equipo():
    if 'username' in session:
        try:
            with open('equipo', 'w') as archivo:
                archivo.truncate()
        except FileNotFoundError:
            return 'No se encuentra el archivo'
        consulta_equipo = Consulta()
        df4 = pd.read_csv('fixture')
        if consulta_equipo.validate_on_submit():
            if consulta_equipo.equipo.data is "":
                return render_template('nulo.html')
            else:
                df5 = df4[(df4['EQUIPO'].str.contains(consulta_equipo.equipo.data))]
                df6 = df5.to_csv('equipo' ,index=None )
                if df5.empty is True:
                    flash('No existe ese equipo')
                    return redirect('/filtro/equipo')
                else:
                    with open('equipo') as archivo:
                        resultado = csv.reader(archivo)
                        encabezado = next(resultado)
                        return render_template('equipo.html',encabezado=encabezado,resultado=resultado)
        return render_template('filtro.html' , consulta_equipo=consulta_equipo)
    return render_template('loguearte.html')

#FILTRO PARA FECHAS
@app.route('/filtro/fecha',methods=['GET' , 'POST'])
def fecha():
    if 'username' in session:
        try:
            with open('fecha', 'w') as archivo:
                archivo.truncate()
        except FileNotFoundError:
            return 'No se encuentra el archivo'
        consulta_fecha = Consulta()
        df7 = pd.read_csv('fixture')
        if consulta_fecha.validate_on_submit():
            if consulta_fecha.fecha.data is "":
                return render_template('nulo.html')
            else:
                df8 = df7[(df7['FECHA'].str.contains(consulta_fecha.fecha.data))]
                df9 = df8.to_csv('fecha' ,index=None )
                if df8.empty is True:
                    flash('No existe esa fecha')
                    return redirect('/filtro/fecha')
                else:
                    with open('fecha') as archivo:
                        date = csv.reader(archivo)
                        head = next(date)
                        return render_template('fecha.html',head=head,date=date)
        return render_template('filtro.html' , consulta_fecha=consulta_fecha)
    return render_template('loguearte.html')

#FILTRO PARA GOLES
@app.route('/filtro/goles',methods=['GET' , 'POST'])
def goles():
    if 'username' in session:
        try:
            with open('filtro', 'w') as archivo:
                archivo.truncate()
        except FileNotFoundError:
            return 'No se encuentra el archivo'
        consulta_goles = Consulta()
        df2 = pd.read_csv('fixture')
        df2.to_csv('filtro' , index = None , header = None)
        with open('filtro') as golazo:
            golazo = csv.reader(golazo)
            listaordenada = sorted(golazo,
                            key=operator.itemgetter(3),
                            reverse=False)
        if consulta_goles.validate_on_submit():
            if consulta_goles.goles.data is "":
                return render_template('nulo.html')
            else:
                df3 = df2[(df2['GOLES'] == (consulta_goles.goles.data))]
                df4 = df3.to_csv('goles' ,index=None )
                if df3.empty is True:
                    return render_template('nulo.html')
                else:
                    with open('goles') as archivo:
                        goal = csv.reader(archivo)
                        cabezazo = next(goal)
                        return render_template('goles.html',goal=goal,cabezazo=cabezazo)
        return render_template('filtro.html' , consulta_goles=consulta_goles,listaordenada=listaordenada)
    return render_template('loguearte.html')

#INFO DE WEB
@app.route('/about',methods=['GET' , 'POST'])
def contacto():
    if 'username' in session:
        return render_template('about.html')
    return render_template('loguearte.html')


#REDIRECCION EN CASO DE ERRORES
@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500

#LOGOUT DE LA WEB
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

#FUNCION PARA EL DATETIME DE LOS ARCHIVOS A EXPORTAR
def tiempoarchivo(fname, fmt='%Y-%m-%d-%H-%M-%S-{fname}'):
        import datetime
        return datetime.datetime.now().strftime(fmt).format(fname=fname)


#BLOQUE DE RUTAS A LA DESCARGA DE ARCHIVOS VIA WEB
@app.route('/download/cancha', methods=['GET', 'POST'])
def bajacancha():
    with open('cancha' , 'r+') as a:
        old = a.read()
        a.seek(0)
        a.write("Consulta sobre las canchas del torneo\n" + old)
        return send_file('cancha', as_attachment=True ,attachment_filename=timeStamped("cancha_.csv" ,'%Y%m%d%H%M%S-{fname}'))

@app.route('/download/equipo', methods=['GET', 'POST'])
def bajaequipo():
    with open('equipo' , 'r+') as a:
        old = a.read()
        a.seek(0)
        a.write("Consulta sobre los equipos del torneo\n" + old)    
        return send_file('equipo', as_attachment=True ,attachment_filename=timeStamped("equipo_.csv" ,'%Y%m%d%H%M%S-{fname}'))

@app.route('/download/fecha', methods=['GET', 'POST'])
def bajafecha():
    with open('fecha' , 'r+') as a:
        old = a.read()
        a.seek(0)
        a.write("Consulta sobre las fechas del torneo\n" + old)
        return send_file('fecha', as_attachment=True ,attachment_filename=timeStamped("fecha_.csv" ,'%Y%m%d%H%M%S-{fname}'))

@app.route('/download/goles', methods=['GET', 'POST'])
def bajagoles():
    with open('goles' , 'r+') as a:
        old = a.read()
        a.seek(0)
        a.write("Consulta sobre la cantidad de goles de cada fecha\n" + old)
        return send_file('goles', as_attachment=True ,attachment_filename=timeStamped("goles_.csv" ,'%Y%m%d%H%M%S-{fname}'))

@app.route('/download/fixture', methods=['GET', 'POST'])
def bajafixture():
    with open('fixture' , 'r+') as a:
        old = a.read()
        a.seek(0)
        a.write("Fixture del torneo\n" + old)
        return send_file('fixture', as_attachment=True ,attachment_filename=timeStamped("fixture_.csv" ,'%Y%m%d%H%M%S-{fname}'))

if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()
