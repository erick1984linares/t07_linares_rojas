# Decodificar mensaje encriptado
# C = Chompas
# P = Polos
# S = Shorts
# H = Chalecos
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "C":
        print("Chompas")
    if letra == "P":
        print("Polos")
    if letra == "S":
        print("Shorts")
    if letra == "H":
        print("Chalecos")
#fin_iterador

print("Fin del bucle")
