#!/usr/bin/python3


print ('BIENVENID@')

ALUMNO_1 = int(input('Si es hombre ingrese 1 si es mujer ingrese 2: '))
ALUMNO_2 = int(input('Si es hombre ingrese 1 si es mujer ingrese 2:'))
ALUMNO_3 = int(input('Si es hombre ingrese 1 si es mujer ingrese 2:'))
ALUMNO_4 = int(input('Si es hombre ingrese 1 si es mujer ingrese 2:'))
ALUMNO_5 = int(input('Si es hombre ingrese 1 si es mujer ingrese 2:'))

if ALUMNO_1 == 1:
    HOMBRE_1 = 1 
    MUJER_1 = 0
else:
    MUJER_1 = 1
    HOMBRE_1 = 0

if ALUMNO_2 == 1:
    HOMBRE_2 = 1 
    MUJER_2 = 0
else:
    MUJER_2 = 1 
    HOMBRE_2 = 0

if ALUMNO_3 == 1:
    HOMBRE_3 = 1 
    MUJER_3 = 0
else:
    MUJER_3 = 1
    HOMBRE_3 = 0

if ALUMNO_4 == 1:
    HOMBRE_4 = 1
    MUJER_4 = 0
else:
    MUJER_4 = 1 
    HOMBRE_4 = 0

if ALUMNO_5 == 1:
    HOMBRE_5 = 1 
    MUJER_5 = 0
else:
    MUJER_5 = 1 
    HOMBRE_5 = 0


HOMBRES = HOMBRE_1 + HOMBRE_2 + HOMBRE_3 + HOMBRE_4 + HOMBRE_5
print ('Los hombres son: ')
print (HOMBRES)
MUJERES = MUJER_1 + MUJER_2 + MUJER_3 + MUJER_4 + MUJER_5
print ('Las mujeres son: ')
print (MUJERES)   






    
    




print ('GRACIAS!!!')



print ('***Desing by @xcabezaderadiox***')
