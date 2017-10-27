Parcial_uno = int(input('La nota del primer parcial fue: '))
Parcial_dos = int(input('La nota del segundo parcial fue: '))
Parcial_tres = int(input('La nota del tercer parcial fue: '))
PROMEDIO_DE_PARCIALES = ((Parcial_uno + Parcial_dos + Parcial_tres) / 3)
print ('EL PROMEDIO DE LOS PARCIALES FUE: ')
print (PROMEDIO_DE_PARCIALES)
EXAMEN_FINAL = int(input('La nota del examen final fue: '))
TP_FINAL = int(input('La nota del trabajo practico final fue: '))
CALIFICACION = ((PROMEDIO_DE_PARCIALES * 0.55) + (EXAMEN_FINAL * 0.30) + (TP_FINAL * 0.15))
print ('SU CALIFICACION FINAL SERA: ')
print (CALIFICACION)


