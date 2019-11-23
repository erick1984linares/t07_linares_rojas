# Decodificar mensaje encriptado
# A = papa
# B = mama
# F = hermanos
# R = primos
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "A":
        print("papa")
    if letra == "B":
        print("mama")
    if letra == "F":
        print("hermanos")
    if letra == "R":
        print("primos")
#fin_iterador

print("Fin del bucle")
