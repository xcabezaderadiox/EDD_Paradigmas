Alumnos = int(input("Por favor ingrese el numero de alumnos: "))
x = 1
m = 0
h = 0
while x <= (Alumnos):
    s = int(input("Ingrese sexo,si es mujer ingrese 1 si es hombre ingrese 2: "))
    if s == 1:
        m = m + 1 
    elif s == 2:
        h = h + 1
    else:
        print ("ERROR")
        break   
    x = x + 1

print ("La cantidad de hombres en el grupo es de " + str(h))
print ("La cantidad de mujeres en el grupo es de " + str(m))
    
	
    



