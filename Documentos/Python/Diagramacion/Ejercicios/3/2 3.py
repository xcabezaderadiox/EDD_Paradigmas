print ('BIENVENID@')

GENERO = int(input('Hola,si el paciente es Hombre inserte 1,si es Mujer ingrese 2:   '))
EDAD = int(input('Por favor ingrese su edad: '))
if GENERO == 1:
    PULSASIONES_CADA_DIEZ_SEGUNDOS_SEGUN_EDAD = (210 - EDAD) / 10
else: 
    PULSASIONES_CADA_DIEZ_SEGUNDOS_SEGUN_EDAD = (220 - EDAD) / 10

print ('Sus pulsaciones cada diez segundos seran de: ')
print (str(PULSASIONES_CADA_DIEZ_SEGUNDOS_SEGUN_EDAD))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')

