print ('BIENVENID@')

PROMEDIO = int(input('Hola por favor ingrese su promedio general:   '))
MATRICULA = int(input('Por favor ingrese el monto de su matricula: '))
if PROMEDIO > 9:
    DESCUENTO = MATRICULA * 0.30
    CUOTA = MATRICULA - DESCUENTO
else: 
    IVA = MATRICULA * 0.21
    IVA_10 = IVA * 0.10
    CUOTA = MATRICULA + IVA_10

print ('La cuota sera de: ')
print (str(CUOTA))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
