listan = []
listap = []
listac = [] 
x = 1
while x <= 20:
    num = int(input("Ingrese numero: "))
    if num % 2 == 0 and num != 0:
        listap.append(num)
    elif num % 2 == 1:
        listan.append(num)
    else:
        listac.append(num)
    x = x +1
print ("Los negativos son: " + str(len(listan))) 
print ("Los positivos son: " + str(len(listap)))
print ("La cantidad de ceros es: " + str( len(listac)))
