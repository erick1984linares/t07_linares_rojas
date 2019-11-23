# Sumar los "y" primeros numeros

import os

#input
y=int(os.sys.argv[1])
i=0

suma=0
while(i<=y):
    suma += i
    i += 1
#fin_while

print("La suma de los 500 primeros numeros es:", suma)
