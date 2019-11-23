#sumar los numeros que estan entre "p" y "q"
import os
#input
p=int(os.sys.argv[1])
q=int(os.sys.argv[2])
i=p
suma=0
while(i<=q):
    suma += i
    i += 1
#fin_while

print("la suma de los numeros impares que estan entre 30 y 90 es:", suma)
