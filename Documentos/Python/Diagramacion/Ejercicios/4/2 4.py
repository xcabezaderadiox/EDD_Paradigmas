print ('BIENVENID@,por favor ingrese 20 numeros')

NUMERO_UNO = int(input(':   '))
NUMERO_DOS = int(input(':   '))
NUMERO_TRES = int(input(':   '))
NUMERO_CUATRO = int(input(':   '))
NUMERO_CINCO = int(input(':   '))
NUMERO_SEIS = int(input(':   '))
NUMERO_SIETE = int(input(':   '))
NUMERO_OCHO = int(input(':   '))
NUMERO_NUEVE = int(input(':   '))
NUMERO_DIEZ = int(input(':   '))
NUMERO_ONCE = int(input(':   '))
NUMERO_DOCE = int(input(':   '))
NUMERO_TRECE = int(input(':   '))
NUMERO_CATORCE = int(input(':   '))
NUMERO_QUINCE = int(input(':   '))
NUMERO_DIECISEIS = int(input(':   '))
NUMERO_DIECISIETE = int(input(':   '))
NUMERO_DIECIOCHO = int(input(':   '))
NUMERO_DIECINUEVE = int(input(':   '))
NUMERO_VEINTE = int(input(':   '))


if NUMERO_UNO == 0:
    RESULTADO_IGUAL_A_CERO_UNO = 1
    RESULTADO_NEGATIVO_UNO = 0
    RESULTADO_POSITIVO_UNO = 0
elif NUMERO_UNO < 0:
    RESULTADO_NEGATIVO_UNO = 1
    RESULTADO_IGUAL_A_CERO_UNO = 0
    RESULTADO_POSITIVO_UNO = 0    
else:        
    RESULTADO_POSITIVO_UNO = 1
    RESULTADO_NEGATIVO_UNO = 0
    RESULTADO_IGUAL_A_CERO_UNO = 0    

if NUMERO_DOS == 0:
    RESULTADO_IGUAL_A_CERO_DOS = 1
    RESULTADO_NEGATIVO_DOS = 0
    RESULTADO_POSITIVO_DOS = 0    
elif NUMERO_DOS < 0:
    RESULTADO_NEGATIVO_DOS = 1
    RESULTADO_POSITIVO_DOS = 0 
    RESULTADO_IGUAL_A_CERO_DOS = 0        
else:        
    RESULTADO_POSITIVO_DOS = 1
    RESULTADO_IGUAL_A_CERO_DOS = 0
    RESULTADO_NEGATIVO_DOS = 0         

if NUMERO_TRES == 0:
    RESULTADO_IGUAL_A_CERO_TRES = 1
    RESULTADO_NEGATIVO_TRES = 0
    RESULTADO_POSITIVO_TRES = 0    
elif NUMERO_TRES < 0:
    RESULTADO_NEGATIVO_TRES = 1
    RESULTADO_POSITIVO_TRES = 0
    RESULTADO_IGUAL_A_CERO_TRES = 0        
else:        
    RESULTADO_POSITIVO_TRES = 1 
    RESULTADO_IGUAL_A_CERO_TRES = 0
    RESULTADO_NEGATIVO_TRES = 0
    
   
    
RESULTADO_POSITIVO = str(int(RESULTADO_POSITIVO_UNO + RESULTADO_POSITIVO_DOS + RESULTADO_POSITIVO_TRES  ))
RESULTADO_NEGATIVO = str(int(RESULTADO_NEGATIVO_UNO + RESULTADO_NEGATIVO_DOS + RESULTADO_NEGATIVO_TRES ))
RESULTADO_IGUAL_A_CERO = str(int(RESULTADO_IGUAL_A_CERO_UNO + RESULTADO_IGUAL_A_CERO_DOS + RESULTADO_IGUAL_A_CERO_TRES ))


print ('Sus numeros estan compuestos de: ')
print (str((RESULTADO_POSITIVO) + ' numeros positivos'))
print (str((RESULTADO_NEGATIVO) + ' numeros negativos'))
print (str((RESULTADO_IGUAL_A_CERO) + ' numeros ceros'))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
