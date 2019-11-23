# Decodificar mensaje encriptado
# A = ZAPATILLAS
# B = ZAPATOS
# F = TACONES
# R = SANDALIAS
msg="ABBFRR"

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
