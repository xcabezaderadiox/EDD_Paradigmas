#!/usr/bin/python3

print ('BIENVENID@,por favor ingrese 20 numeros')

def funcion1():
    Numero = int(input('Ingrese numero: '))
    
    if Numero == 0:
        global RESULTADO_IGUAL_A_CERO
        RESULTADO_IGUAL_A_CERO =  RESULTADO_IGUAL_A_CERO +  1       
    elif Numero < 0:
        global RESULTADO_NEGATIVO
        RESULTADO_NEGATIVO = RESULTADO_NEGATIVO + 1
    else:  
        global RESULTADO_POSITIVO      
        RESULTADO_POSITIVO = RESULTADO_POSITIVO + 1

RESULTADO_POSITIVO = 0
RESULTADO_NEGATIVO = 0
RESULTADO_IGUAL_A_CERO = 0   
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()
funcion1()


print ('Sus numeros estan compuestos de: ') 
print ('Numeros positivos')       
print (RESULTADO_POSITIVO)
print ('Numeros negativos')
print (RESULTADO_NEGATIVO)
print ('numeros igual a cero')
print (RESULTADO_IGUAL_A_CERO)
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')



