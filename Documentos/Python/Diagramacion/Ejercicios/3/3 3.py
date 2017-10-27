print ('BIENVENID@')

SEGURO = int(input('Hola por favor ingrese el monto de su seguro:   '))
if SEGURO > 50000:
    CUOTA_DEL_SEGURO = SEGURO * 0.03
else: 
    CUOTA_DEL_SEGURO = SEGURO * 0.02

print ('La cuota de su seguro sera de: ')
print (str(CUOTA_DEL_SEGURO))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
