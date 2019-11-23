# Imprimir los numeros que hay entre "k" y "n" multiplicados por 3
import os
#input
k=int(os.sys.argv[1])
n=int(os.sys.argv[2])
#iterador
for i in range(k, n):
    print((i)*3)
#fin_iterador_en_rango

print("Fin del bucle")
