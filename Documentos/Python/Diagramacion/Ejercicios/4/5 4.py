#!/usr/bin/python3


print ('BIENVENID@')

def auto():
    global Puntos
    global Punto_1
    global Punto_2
    global Punto_3
    global Tutu
    Tutu = Tutu + 1
    print ('Ingrese datos del auto numero ' + str(Tutu))
    Punto_1 = int(input('Ingrese contaminante del primer punto: '))
    Punto_2 = int(input('Ingrese contaminante del segundo punto: '))
    Punto_3 = int(input('Ingrese contaminante del tercer punto: ')) 
    global Puntos_a
    global Puntos_b
    global Puntos_c
    global Punto_mas_contaminante
    global Punto_menos_contaminante
    Puntos_a = Punto_1 + Puntos_a 
    Puntos_b = Punto_2 + Puntos_b
    Puntos_c = Punto_3 + Puntos_c
    Puntos = Puntos + Punto_1 + Punto_2 + Punto_3 
    if Puntos_a > Puntos_b and Puntos_a > Puntos_c:
        Punto_mas_contaminante = 'Es el punto a con un total de ' + str(Puntos_a)
    if Puntos_b > Puntos_a and Puntos_b > Puntos_c:
        Punto_mas_contaminante = 'Es el punto b con un total de ' + str(Puntos_b)
    if Puntos_c > Puntos_a and Puntos_c > Puntos_b:
        Punto_mas_contaminante = 'Es el punto c con un total de ' + str(Puntos_c)
    if Puntos_a < Puntos_b and Puntos_a < Puntos_c:
        Punto_menos_contaminante = 'Es el punto a con un total de ' + str(Puntos_a)
    if Puntos_b < Puntos_a and Puntos_b < Puntos_c:
        Punto_menos_contaminante = 'Es el punto b con un total de ' + str(Puntos_b)
    if Puntos_c < Puntos_a and Puntos_c < Puntos_b:
        Punto_menos_contaminante = 'Es el punto c con un total de ' + str(Puntos_c)

Puntos = 0     
Tutu = 0
Puntos_a = 0
Puntos_b = 0
Puntos_c = 0

for _ in range (0,25):
    auto()





Promedio = Puntos / 25
print ('El promedio de contaminantes es: ')
print (Promedio)
print ('El punto mas contaminante es: ')
print (Punto_mas_contaminante)
print ('El punto menos contaminante es: ')
print (Punto_menos_contaminante)

print ('GRACIAS!!!')



print ('***Desing by @xcabezaderadiox***')
