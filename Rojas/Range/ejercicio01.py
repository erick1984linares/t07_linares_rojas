import os
#Mostrar el cuadrado de los 10 primeros numeros naturales
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

for x in range(y):
    print("Ahora x vale", x,"y su cuadrado",(x**2))
    x+=1

#Fin_iterador_rango
print("fin del bucle")
