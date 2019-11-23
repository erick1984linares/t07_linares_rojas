# Imprimir los "X" primeros numeros sumados por n mientras "n" sea cualquier entero positivo y dividir entre 4
import os
#input
x=int(os.sys.argv[1])
n=2
#iterador
for i in range(x):
    print((i*n)/4)
#fin_iterador_en_rango

print("Fin del bucle")
