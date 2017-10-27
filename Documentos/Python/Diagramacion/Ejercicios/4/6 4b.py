lista = []
x = 1
while x <= 5:
    t = int(input("Ingrese km: "))
    lista.append(t)
    x = x + 1
    if t > int(16):
        print ("FALLO")
        break
    elif t < int(13):
        print ("Meta de 13 minutos alcanzada")
if len(lista) == int(5):
    if prom <= int(15):
            print ("FELICITACIONES ESTA APTO")
    
	
    



