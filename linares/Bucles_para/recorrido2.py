#sumar los numeros que estan entre "m" y "n"
import os
#input
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])
i=m
suma=0
while(i<=n):
    suma += i
    i += 1
#fin_while

print("La suma de los numeros que estan entre 55 y 125 es:", suma)
