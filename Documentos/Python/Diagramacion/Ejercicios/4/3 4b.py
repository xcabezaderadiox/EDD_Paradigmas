lista = []
x = 1
while x <= 40:
    num = int(input("Ingrese nota: "))
    lista.append(num)
    x = x +1
print ("La menor nota es: " + str(min(lista))) 
print ("El promedio general es: " + str(sum(lista) / len(lista)))
