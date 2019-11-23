
#sumar los numeros que estan entre "a" y "b"
import os
#input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
i=a
suma=0
while(i<=b):
    suma += i
    i += 1
#fin_while

print("La suma de los numeros que estan entre 20 y 80 es:", suma)
