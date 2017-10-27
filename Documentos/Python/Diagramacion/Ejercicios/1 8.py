Alumnos = int(input("Por favor ingrese la cantidad de alumnos por grupo: "))
Grupos = int(input("Por favor ingrese la cantidad de grupos: "))
listapa = []
n = 0
for _ in range(Grupos):   
    for _ in range(Alumnos):
        Nota_1 = int(input("Por favor ingrese el resultado de la primer nota: "))
        Nota_2 = int(input("Por favor ingrese el resultado de la segunda nota: "))
        Nota_3 = int(input("Por favor ingrese el resultado de la tercer nota: "))
        Promedio_alumno = (Nota_1 + Nota_2 + Nota_3) / 3
        listapa.append(Promedio_alumno)
        listapg.append(Promedio_alumno)
        print ("El promedio del alumno fue " + str(Promedio_alumno))
    
        
              
Promedio_general = (sum(listapa) / len(listapa))
print ("El promedio general de los grupos fue: " + str(Promedio_general))
    
	
    



