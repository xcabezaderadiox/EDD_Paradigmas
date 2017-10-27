print ('BIENVENID@ A TIENDA COMPUCHRIS')

COMPRA = int(input('Ingrese su compra: '))

if COMPRA > 2000:
    PC_YNOS = str(input('Usted compro una YNOS?'))
    if PC_YNOS == 'si':
        PRECIO_FINAL = (COMPRA - (COMPRA * 0.15))
    else: 
        PRECIO_FINAL = (COMPRA - (COMPRA * 0.10))
else:
    PRECIO_FINAL = (COMPRA + (COMPRA * 0.21))    

print ('Su valor final de compra es de: ')   
print (PRECIO_FINAL)
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
