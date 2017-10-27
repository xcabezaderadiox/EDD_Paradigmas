#!/usr/bin/python3


print ('BIENVENID@')

def Notas():
    Nota = int(input('Ingrese nota del alumno: '))
    global PROMEDIO
    PROMEDIO = PROMEDIO + Nota 
    global NOTA_MAS_BAJA
    if NOTA_MAS_BAJA > Nota:
        NOTA_MAS_BAJA = Nota
    
PROMEDIO = 0
NOTA_MAS_BAJA = 10

for _ in range (0,40):
    Notas()


PROMEDIO_GENERAL = PROMEDIO / 40 
print ('Los resultados son: ') 
print ('Promedio general')       
print (PROMEDIO_GENERAL)
print ('Nota mas baja')
print (NOTA_MAS_BAJA)

print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
