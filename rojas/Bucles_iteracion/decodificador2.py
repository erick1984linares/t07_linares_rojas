# Decodificar mensaje encriptado
# A = Los dias de la semana son:
# B = Lunes
# F = Martes
# R = Mircoles
# M = Jueves
# P = Viernes
# Q = Sabado
# S = Domingo
msg="AABFRMPQS"

for letra in msg:
    if letra == "A":
        print("Los dias de la semana son:")
    if letra == "B":
        print("Lunes")
    if letra == "F":
        print("Martes")
    if letra == "R":
        print("Mircoles")
    if letra == "M":
        print("Jueves")
    if letra == "P":
        print("Viernes")
    if letra == "Q":
        print("Sabado")
    if letra == "S":
        print("Domingo")
#fin_iterador

print("Fin del bucle")
