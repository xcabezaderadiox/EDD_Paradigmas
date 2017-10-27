numero = int(input("Ingrese el numero: "))
for _ in range(0,10000000000000):
    if numero >= 0:
        numero = int(input("Ingrese otro numero "))
    else:
        print ("El numero es negativo!")
        break
