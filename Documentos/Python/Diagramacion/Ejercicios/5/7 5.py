Meses = int(input("Por favor ingrese los meses a  invertir:"))
Numero = int(input("Por favor ingrese el dinero a  invertir:"))
Interes = 0.02
n = 1
while n <= Meses:
    Ganancia = Numero * Interes
    n = n + 1
    Valor = Ganancia + Numero
    
print ("Su ganancia al cabo del tiempo invertido sera de " + str(Valor))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
