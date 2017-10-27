Clientes = int(input("Por favor ingrese la cantidad de clientes que hubo:"))
n = 1
Valor_total = 0
while n <= Clientes:
    Compra = int(input("Por favor ingrese el valor de compra: "))
    Valor_total = Compra + Valor_total
    n = n + 1
    
print ("Lo recaudado en ventas en el dia fue " + str(Valor_total))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
