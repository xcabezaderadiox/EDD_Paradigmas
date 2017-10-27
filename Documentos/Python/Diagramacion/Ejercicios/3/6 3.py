print ('BIENVENID@')

HECTAREAS = int(input('Hola por favor ingrese su cantidad de hectareas:   '))
HECTAREA = HECTAREAS * 10000
if HECTAREAS > 1000000:
    PINOS = ((HECTAREA * 0.70) / 10) * 8 
    OYAMELES = ((HECTAREA * 0.20) / 15) * 15
    CEDROS = ((HECTAREA * 0.10) / 18) * 10
    
else: 
    PINOS = ((HECTAREA * 0.50) / 10) * 8 
    OYAMELES = ((HECTAREA * 0.30) / 15) * 15
    CEDROS = ((HECTAREA * 0.20) / 18) * 10

print ('La cantidad de pinos sera de: ')
print (str(PINOS))
print ('La cantidad de oyameles sera de: ')
print (str(OYAMELES))
print ('La cantidad de cedros sera de: ')
print (str(CEDROS))
print ('GRACIAS!!!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
