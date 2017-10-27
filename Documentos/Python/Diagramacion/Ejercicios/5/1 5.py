#!/usr/bin/python3


print ('BIENVENID@')

VENDEDORES = int(input('Ingrese la cantidad de vendedores que hay: '))
SUELDO_BASE = 10000

VALOR_DE_VENTAS = SUELDO_BASE * 0.30
print ('El vendedor se lleva ' + (str(VALOR_DE_VENTAS)) + ' pesos por comisiones')

SUELDO_TOTAL = SUELDO_BASE + VALOR_DE_VENTAS
print ('El sueldo total por mes mas las 3 ventas es de ' + (str(SUELDO_TOTAL)) + ' pesos')


PAGO_TOTAL_DE_COMISIONES = VALOR_DE_VENTAS * VENDEDORES
print ('El costo de pago general por comisiones a todos los vendedores sera de ' + (str(PAGO_TOTAL_DE_COMISIONES)) + ' pesos')

PAGO_TOTAL_DE_SUELDOS = SUELDO_TOTAL * VENDEDORES
print ('El costo de sueldo de todos los vendedores sera de ' + (str(PAGO_TOTAL_DE_SUELDOS)) + ' pesos')

    
    




print ('GRACIAS!!!')



print ('***Desing by @xcabezaderadiox***')
