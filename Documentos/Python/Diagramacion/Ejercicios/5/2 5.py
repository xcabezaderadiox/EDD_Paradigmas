#!/usr/bin/python3


print ('BIENVENID@')

OBREROS = int(input('Ingrese la cantidad de obreros que hay: '))
HORAS = int(input('Cuantas horas trabajo?'))
EXTRAS = int(input('Cuantas horas extras trabajo?'))

VALOR_EXTRAS = EXTRAS * 25

if HORAS < 40:
    SUELDO = HORAS * 20
    print (SUELDO)
else:
    SUELDO = HORAS * 20 + VALOR_EXTRAS
    print (SUELDO)


    
    




print ('GRACIAS!!!')



print ('***Desing by @xcabezaderadiox***')
