#sumar los que estan entre "x" y "y"
import os
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
i=x
suma=0
while(i<=y):
    suma += i
    i += 1
#fin_while

print("la suma de los numeros que estan entre 120 y 200 :", suma)
