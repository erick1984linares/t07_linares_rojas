# Sumar los "X" numeros desde 35 hasta 135

import os

#input
X=int(os.sys.argv[1])
i=0

suma=0
while(i<=X):
    suma += i
    i += 1
#fin_while

print("La suma de los 100 primeros numeros es:", suma)
