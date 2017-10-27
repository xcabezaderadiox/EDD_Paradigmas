print ('BIENVENID@ ALUMNO!!!')

PROMEDIO = int(input('Por favor ingrese su promedio:   '))
CICLO = int(input('Ingrese si es del primer ciclo un 1 y si es del segundo ciclo un 2:   '))
MATERIAS_REPROBADAS = int(input('Por favor ingrese la cantidad de materias reprobadas que tiene: '))

MATRICULA_CICLO_UNO = 180
MATRICULA_CICLO_DOS = 300

if PROMEDIO >= 9.5: 
    if CICLO == 1:
        print('Podra cursar 55 unidades y su valor sera de:')
        print (str((MATRICULA_CICLO_UNO * 11) - ((MATRICULA_CICLO_UNO * 11) * 0.25)))        
    else:
        print('Podra cursar 25 unidades y su valor sera de: ')     
        print (str((MATRICULA_CICLO_DOS * 5 ) -((MATRICULA_CICLO_DOS * 5) * 0.20)))

if PROMEDIO <= 9.5: 
    if CICLO == 2:
        print('Podra cursar 25 unidades y su valor sera de:')
        print (str(MATRICULA_CICLO_DOS * 5))

if PROMEDIO >= 9 and PROMEDIO < 9.5: 
    if CICLO == 1:
        print('Podra cursar 50 unidades y su valor sera de:')
        print (str((MATRICULA_CICLO_UNO * 10) - ((MATRICULA_CICLO_DOS * 5) * 0.10)))

if PROMEDIO >= 7 and PROMEDIO < 9: 
    if CICLO == 1:
        print('Podra cursar 50 unidades y su valor sera de:')
        print (str((MATRICULA_CICLO_UNO * 10)))

if PROMEDIO <= 7: 
    if CICLO == 1:
        if MATERIAS_REPROBADAS <= 3:
            print('Podra cursar 45 unidades y su valor sera de:')
            print (str((MATRICULA_CICLO_UNO * 9)))

if PROMEDIO <= 7: 
    if CICLO == 1:
        if MATERIAS_REPROBADAS >= 4:
            print('Podra cursar 40 unidades y su valor sera de:')
            print (str((MATRICULA_CICLO_UNO * 8)))
 
                  


print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
