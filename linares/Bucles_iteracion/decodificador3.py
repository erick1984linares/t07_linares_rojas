# Decodificar mensaje encriptado
# A = ZAPATILLAS
# B = ZAPATOS
# F = TACONES
# R = SANDALIAS
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "A":
        print("Zapatillas")
    if letra == "B":
        print("Zapatos")
    if letra == "F":
        print("Tacones")
    if letra == "R":
        print("Sandalias")
#fin_iterador

print("Fin del bucle")
