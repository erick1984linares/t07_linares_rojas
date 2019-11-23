# Decodificar mensaje encriptado
# 9 = Illimo
# 8 = Tucume
# 7 = Pacora
# 6 = Mochumi
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "9":
        print("Illimo")
    if letra == "8":
        print("Tucume")
    if letra == "7":
        print("Pacora")
    if letra == "6":
        print("Muchumi")
#fin_iterador

print("Fin del bucle")
