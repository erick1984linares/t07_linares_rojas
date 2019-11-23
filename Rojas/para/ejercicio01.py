# Sumar los "q"  numeros desde 20

import os

#input
q=int(os.sys.argv[1])
i=20

suma=0
while(i<=q):
    suma += i
    i += 1
#fin_while

print("La suma de los 100 primeros numeros despues de 20 es:", suma)
