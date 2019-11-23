#sumar los numeros que hay desde "M" hasta "N" pares
import os
#input
M=int(os.sys.argv[1])
N=int(os.sys.argv[2])
i=M
suma=0
while(i<=N):
    suma += i
    i += 2
#fin_while

print("la suma de los numeros que hay desde 100 hasta 660 es:", suma)
