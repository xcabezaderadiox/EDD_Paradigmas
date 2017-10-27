print ('BIENVENID@ AL ADIVINADOR DE NUMEROS MEDIOS MAS INCREIBLE')

NUMERO_UNO = int(input('Por favor ingrese el primer numero: '))
NUMERO_DOS = int(input('Por favor ingrese el segundo numero: '))
NUMERO_TRES = int(input('Por favor ingrese el tercer numero: '))

if NUMERO_UNO > NUMERO_DOS and NUMERO_UNO < NUMERO_TRES:
    print (NUMERO_UNO)

if NUMERO_UNO < NUMERO_DOS and NUMERO_UNO > NUMERO_TRES:
    print (NUMERO_UNO)

if NUMERO_DOS > NUMERO_UNO and NUMERO_DOS < NUMERO_TRES:
    print (NUMERO_DOS)

if NUMERO_DOS < NUMERO_UNO and NUMERO_DOS > NUMERO_TRES:
    print (NUMERO_DOS)

if NUMERO_TRES > NUMERO_UNO and NUMERO_TRES < NUMERO_DOS:
    print (NUMERO_TRES)

if NUMERO_TRES < NUMERO_UNO and NUMERO_TRES > NUMERO_DOS:
    print (NUMERO_TRES)


print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
