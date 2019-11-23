#sumar los numeros que hay desde "A" hasta "B"
import os
#input
A=int(os.sys.argv[1])
B=int(os.sys.argv[2])
i=A
suma=0
while(i<=B):
    suma += i
    i += 1
#fin_while

print("la suma de los numeros que hay desde 200 hasta 1350 es:", suma)
