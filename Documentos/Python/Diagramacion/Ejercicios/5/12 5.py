
Gordo_1 = int(input("Por favor ingrese el peso incial del primer obeso: "))
Gordo_2 = int(input("Por favor ingrese el peso incial del segundo obeso: "))
Gordo_3 = int(input("Por favor ingrese el peso incial del tercer obeso: "))
Gordo_4 = int(input("Por favor ingrese el peso incial del cuarto obeso: "))
Gordo_5 = int(input("Por favor ingrese el peso incial del quinto obeso: "))
Valor_total_1 = 0
Valor_total_2 = 0
Valor_total_3 = 0
Valor_total_4 = 0
Valor_total_5 = 0
n = 1
Cantidad_de_pesajes = 5
while n <= Cantidad_de_pesajes:
    Pesaje_1 = int(input("Por favor ingrese el pesaje del gordo uno: "))
    Pesaje_2 = int(input("Por favor ingrese el pesaje del gordo dos: "))
    Pesaje_3 = int(input("Por favor ingrese el pesaje del gordo tres: "))
    Pesaje_4 = int(input("Por favor ingrese el pesaje del gordo cuatro: "))
    Pesaje_5 = int(input("Por favor ingrese el pesaje del gordo cinco: "))
    Valor_total_1 = Gordo_1 - Pesaje_1
    Valor_total_2 = Gordo_2 - Pesaje_2
    Valor_total_3 = Gordo_3 - Pesaje_3
    Valor_total_4 = Gordo_4 - Pesaje_4
    Valor_total_5 = Gordo_5 - Pesaje_5
    n = n + 1
    
Diferencia_1 = Gordo_1 - Valor_total_1
if Diferencia_1 < Gordo_1:
    print ("El gordo uno bajo" + (str(Valor_total_1)) + "kilos" )
else:
    print ("El gordo uno subio " + (str(-1 * Valor_total_1)) + " kilos" )

Diferencia_2 = Gordo_2 - Valor_total_2
if Diferencia_2 < Gordo_2:
    print ("El gordo dos bajo" + (str(Valor_total_2)) + "kilos" )
else:
    print ("El gordo dos subio " + (str(-1 * Valor_total_2)) + " kilos" )

Diferencia_3 = Gordo_3 - Valor_total_3
if Diferencia_3 < Gordo_3:
    print ("El gordo tres bajo" + (str(Valor_total_3)) + "kilos" )
else:
    print ("El gordo tres subio " + (str(-1 * Valor_total_3)) + " kilos" )

Diferencia_4 = Gordo_4 - Valor_total_4
if Diferencia_4 < Gordo_4:
    print ("El gordo cuatro bajo" + (str(Valor_total_4)) + "kilos" )
else:
    print ("El gordo cuatro subio " + (str(-1 * Valor_total_4)) + " kilos" )

Diferencia_5 = Gordo_5 - Valor_total_5
if Diferencia_5 < Gordo_5:
    print ("El gordo cinco bajo" + (str(Valor_total_5)) + "kilos" )
else:
    print ("El gordo cinco subio " + (str(-1 * Valor_total_5)) + " kilos" )

print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
