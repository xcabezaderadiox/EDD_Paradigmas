print ('BIENVENID@')

CAPITAL = int(input('Hola por favor ingrese su capital actual:   '))
PCS = 5000
MOBILIARIO = 2000
PRESTAMO = 10000
PRESTAMO_DOS = 20000
if CAPITAL < 0:
    PRESUPUESTO = CAPITAL + PRESTAMO
    print ('Su presupuesto sera de : ')
    print (PRESUPUESTO)
    RESTO = PRESUPUESTO - PCS - MOBILIARIO
    INSUMOS = RESTO / 2
    INCENTIVO = RESTO / 2
    print ('El valor de sus insumos e incentivo laboral seran: ')
    print (INSUMOS)
    print (INCENTIVO) 

elif CAPITAL > 0 and CAPITAL < 20000:
    PRESUPUESTO = CAPITAL + PRESTAMO_DOS
    print ('Su presupuesto sera de: ')
    print (PRESUPUESTO)
    RESTO = PRESUPUESTO - PCS - MOBILIARIO
    INSUMOS = RESTO / 2
    INCENTIVO = RESTO / 2
    print ('El valor de sus insumos e incentivo laboral seran: ')
    print (INSUMOS)
    print (INCENTIVO) 
    
else:
    PRESTAMO = 0
    PRESUPUESTO = CAPITAL + PRESTAMO
    print ('Su presupuesto sera de: ')
    print (PRESUPUESTO)
    RESTO = PRESUPUESTO - PCS - MOBILIARIO
    INSUMOS = RESTO / 2
    INCENTIVO = RESTO / 2
    print ('El valor de sus insumos e incentivo laboral seran: ')
    print (INSUMOS)
    print (INCENTIVO)     

print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
