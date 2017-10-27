print ('BIENVENID@ CONDUCTOR')

def auto():    
    Patente = input('Por favor ingrese patente del auto: ')
    global Resultado
    global Amarilla
    global Roja
    global Rosa
    global Verde
    global Azul
    Resultado = Patente[4]
    if Resultado == "1" or Resultado == "2":
        print ('Es Amarilla')
        Amarilla = Amarilla + 1
    elif Resultado == "3" or Resultado == "4":
        print ('Es Roja')
        Roja = Roja + 1
    elif Resultado == "5" or Resultado == "6":
        print ('Es Rosa')
        Rosa = Rosa + 1        
    elif Resultado == "7" or Resultado == "8":
        print ('Es Verde')
        Verde = Verde + 1
    else:
        Resultado == "9" or Resultado == "0"   
        print ('Es Azul')
        Azul = Azul + 1     



Amarilla = 0
Roja = 0
Rosa = 0
Verde = 0
Azul = 0



for _ in range (0,5):
    auto()

print ('Calcomanias Amarillas: ' + str(Amarilla))
print ('Calcomanias Roja: ' + str(Roja))
print ('Calcomanias Rosa: ' + str(Rosa))
print ('Calcomanias Verde: ' + str(Verde))
print ('Calcomanias Azul: ' + str(Azul))

print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')


