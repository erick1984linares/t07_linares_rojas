#sumar los que estan entre "-k" y "k"
import os
#input
negativo_k=int(os.sys.argv[1])
k=int(os.sys.argv[2])
i=negativo_k
suma=0
while(i<=k):
    suma += i
    i += 1
#fin_while

print("la suma de los numeros que estan entre -30 y 30 :", suma)
