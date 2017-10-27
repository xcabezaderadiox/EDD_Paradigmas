#!/usr/bin/python3


print ('BIENVENID@')

def Func():
    global Multiplicador
    Multiplicador = Multiplicador + 1 
    global Resultado
    Resultado = Numero * Multiplicador 
    print (str(Numero) + 'x' + str(Multiplicador) + '=' + str(Resultado)) 
    

Multiplicador = 0
Resultado = 0
Numero = int(input('Ingrese el numero: '))
print ('La tabla de multiplicar del numero '  + str(Numero) + ' es la siguiente:') 

for _ in range (0,10): 
    Func()




 


print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
