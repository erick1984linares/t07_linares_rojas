# Decodificar mensaje encriptado
# a = enero
# b = febrero
# c = marzo
# d = abril
# e = mayo
# f = junio
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "a":
        print("enero")
    if letra == "b":
        print("febrero")
    if letra == "c":
        print("marzo")
    if letra == "d":
        print("abril")
    if letra == "e":
        print("mayo")
    if letra == "f":
        print("junio")
#fin_iterador

print("Fin del bucle")
