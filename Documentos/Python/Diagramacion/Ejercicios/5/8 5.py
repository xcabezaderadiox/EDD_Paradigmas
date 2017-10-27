Alumnos = int(input("Por favor ingrese la cantidad de alumnos:"))
Hombre = 0
Mujer = 0
Edad_hombre = 0
Edad_mujer = 0
n = 1

while n <= Alumnos:
    Edad = int(input("Por favor ingrese su edad: "))
    Genero = int(input("Por favor si es Hombre ingrese 1 si es mujer ingrese 2: "))
    if Genero == 1:
        Hombre = Hombre + 1
        Edad_hombre = Edad + Edad_hombre
    else:
        Mujer = Mujer + 1
        Edad_mujer = Edad + Edad_mujer
    n = n + 1

Promedio_edad_hombres = Edad_hombre / Hombre
Promedio_edad_mujeres = Edad_mujer / Mujer
Promedio_general_de_edad = (Promedio_edad_hombres + Promedio_edad_mujeres) / 2
    
    
print ("La cantidad de hombres es de " + str(Hombre))
print ("Su promedio de edad sera de " + str(Promedio_edad_hombres))
print ("La cantidad de mujeres es de " + str(Mujer))
print ("Su promedio de edad sera de " + str(Promedio_edad_mujeres))
print ("El promedio de edad general de los alumnos sera de " + str(Promedio_general_de_edad))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
