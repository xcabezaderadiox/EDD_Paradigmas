print ('BIENVENID@')

COMPRA = int(input('Hola por favor ingrese su cantidad de PC compradas:   '))
PC = 1600
if COMPRA < 5:
    PRECIO_FINAL = (PC -(PC * 0.10)) 

elif COMPRA > 5 and COMPRA < 10:
    PRECIO_FINAL = (PC -(PC * 0.20))
    
else:
    PRECIO_FINAL = (PC-(PC * 0.40))    

print ('Su valor final de compra es de: ')   
print (PRECIO_FINAL)
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
