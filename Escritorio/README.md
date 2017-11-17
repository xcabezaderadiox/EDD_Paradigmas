Final_EDD_Paradigmas

INFORME DEL Final

Para el final se agrego la funcionalidad de descarga de archivos en las consultas y el posible reset de password del usuario.

-A grandes rasgos, ¿cómo será el flujo del programa? 
El flujo del programa parte desde un archivo "VelezWeb.py" en donde estan armadas los diferentes approute necesarios para el funcionamiento correcto de la web. Cada approute sera llamado segun el requerimiento del usuario de la web y estos llamaran a su vez a unos .html que estan ubicados en la carpeta templete. Intente crear varios de ellos para ofrecer mejor visualizacion del usuario y dividir bien los temas. Luego en el proyecto tambien se podra observar 5 archivos de texto los cuales cumplen diferentes funciones,mayormente de validacion de datos y base de datos para trabajar con la tabla a mostrar.

-¿Qué estructura se utilizará para representar la información del archivo? 
Este archivo contiene una primer parte con las apps a importar (ejemplo,csv,flask,pandas,etc),luego hay un bloque de referencias y entradas de datos como formularios,clases y una lista creada para la validacion de usuario. Finalmente hay un tercer bloquee donde se encuentran todos los approute.
Se agregaron para el final diferentes approute para bajar las consultas a archivos y tambien otro approute para el reset de pass.

-¿Cómo se usa el programa? 
Su uso en si es bastante sencillo,solo se debe tener en cuenta en principio tener instaladas las apps a usar las cuales son importadas al comienzo del .py. Creamos una carpeta donde estara el .py,y los archivos de texto y luego tambien creamos dentro otra carpeta llamada templates para guardar los .html Una vez que tenemos esto vamos a nuestro entorno virtual y ejecutamos el archivo de la siguiente manera. python3 VelezWeb.py runserver Una vez ejecutado esto el programa deberia arrancar asi que nos dirigimos al home de la web con la siguiente url local para la prueba. http://127.0.0.1:5000/ Finalmente ya estamos listos para navegar la web.

-¿Qué clases se diseñaron?¿Por qué? 
Se crearon 3 clases MiFormulario,Alta y Consulta. La funcion de las primeras dos es la validacion de datos para ya sea el alta de un usuario y su login en la web. La tercera es usada para la solicitud del filtro del Fixture.
Para el final se agrego una clase mas llamada Reset para la validacion de datos en el reset de pass de usuario.

-NOTA Deje dentro de la carpeta del proyecto otra carpeta que se llama PASO A PASO,ahi para que se vea todo el desarrollo de como fui avanzando.

LINK A WEB PYTHON ANYWHERE
http://xcabezaderadiox.pythonanywhere.com/
