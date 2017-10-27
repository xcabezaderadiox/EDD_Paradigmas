print ('BIENVENID@ MAESTRO')

def notas():    
    Calificacion = int(input('Por favor ingrese calificacion de alumno: '))
    global Nota
    Nota = Calificacion + Nota
    
       




Nota = 0




for _ in range (0,5):
    notas()

Promedio = Nota / 5

print ('El promedio de calificaciones es: ' + str(Promedio))


print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')


