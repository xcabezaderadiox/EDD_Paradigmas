#!/usr/bin/python3


print ('BIENVENID@')

DIA_1 = int(input('Ingrese minutos del dia uno: '))
DIA_2 = int(input('Ingrese minutos del dia dos: '))
DIA_3 = int(input('Ingrese minutos del dia tres: ')) 
DIA_4 = int(input('Ingrese minutos del dia cuatro: '))
DIA_5 = int(input('Ingrese minutos del dia cinco: '))

PROMEDIO = (DIA_1 + DIA_2 + DIA_3 + DIA_4 + DIA_5) / 5

if DIA_1 and DIA_2 and DIA_3 and DIA_4 and DIA_5 < 16:
    META_2 = 1
else:
    print ('Mejore sus marcas y vuelva a intentarlo')
    META_2 = 0

if DIA_1 or DIA_2 or DIA_3 or DIA_4 or DIA_5 < 13:
    META = 1
else:
    print ('Mejore sus marcas y vuelva a intentarlo')
    META = 0

if PROMEDIO <= 15 and META == 1 and META_2 == 1:
    print ('Meta cumplida!')
else:
    print ('Aun no esta preparado!')

    
    




print ('GRACIAS!!!')



print ('***Desing by @xcabezaderadiox***')
