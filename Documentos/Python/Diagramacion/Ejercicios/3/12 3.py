print ('BIENVENID@')

SEXO = int(input('Ingrese su sexo,en caso que sea Mujer ingrese 1,si es hombre ingrese 2:   '))
HEMOGLOBINA = int(input('Ingrese su nivel de hemoglobina:   '))
EDAD = int(input('Hola por favor ingrese su edad,en caso que tenga menos de un año ingrese 0:   '))

if EDAD == 0: 
    MESES = int(input('Ingrese su cantidad de meses:   '))
    if MESES <= 1:
        if HEMOGLOBINA > 13:
            print('No tiene anemia') 
        else:
            print('Tiene Ànemia ')     
    if MESES > 1 and MESES <=6:
        if HEMOGLOBINA > 10: 
            print('No tiene anemia')           
        else:
            print('Tiene Ànemia ')
    if MESES > 6 and MESES <= 12:
        if HEMOGLOBINA > 11:
            print('No tiene anemia')   
        else:
            print('Tiene Ànemia ')
                                
                
if EDAD > 1 and EDAD <= 5:
    if HEMOGLOBINA > 11.5:
        print ('No tiene anemia')   
    else:
        print ('Tiene Ànemia ')

if EDAD > 5 and EDAD <= 10:
    if HEMOGLOBINA > 12.6:
        print ('No tiene anemia')   
    else:
        print ('Tiene Ànemia ')

if EDAD > 10 and EDAD <= 15:
    if HEMOGLOBINA > 13:
        print ('No tiene anemia')   
    else:
        print ('Tiene Ànemia ')

if EDAD > 15: 
    if SEXO == 1:
        if HEMOGLOBINA > 12:
            print ('No tiene anemia')   
        else:
            print ('Tiene Ànemia ')
    if SEXO == 2:
        if HEMOGLOBINA > 16:        
            print ('No tiene anemia')   
        else:
            print ('Tiene Ànemia ')                   


print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
