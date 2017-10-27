print ('BIENVENID@')

COMPRA = int(input('Hola por favor ingrese su cantidad de KG de Manzanas compradas:   '))
PRECIO_POR_KILO = 5
if COMPRA <= 2:
    PRECIO_FINAL = (PRECIO_POR_KILO * COMPRA) 

elif COMPRA > 2 and COMPRA <= 5:
    PRECIO_FINAL = (PRECIO_POR_KILO * COMPRA -(PRECIO_POR_KILO * COMPRA * 0.10))

elif COMPRA > 5 and COMPRA <= 10:
    PRECIO_FINAL = (PRECIO_POR_KILO * COMPRA -(PRECIO_POR_KILO * COMPRA * 0.15))
    
else:
    PRECIO_FINAL = (PRECIO_POR_KILO * COMPRA -(PRECIO_POR_KILO * COMPRA * 0.20))    

print ('Su valor final de compra es de: ')   
print (PRECIO_FINAL)
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
