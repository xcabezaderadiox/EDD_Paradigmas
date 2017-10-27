def contar_pares(lista):
    x = 0
    for numero in lista:
        if numero%2 == 0:
            x = x + 1
    print (x)

contar_pares([ 1, 2, 3, 4, 5, 6, 7, 8, 9])

