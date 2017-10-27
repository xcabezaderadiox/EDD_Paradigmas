lista = []
Cantidad = int(input("Por favor ingrese la cantidad de numeros a ingresar:"))
n = 1
while n <= Cantidad:
    lista.append(int(input("Ingrese numero: ")))
    n = n + 1


print ("El menor numero de la lista es: "(min(lista)))
print ("El mayor numero de la lista es: "(max(lista)))
