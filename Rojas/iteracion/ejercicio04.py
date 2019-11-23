# Decodificar mensaje encriptado
# 1 = mar
# 2 = costa
# 3 = sierra
# 4 = selva
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "1":
        print("mar")
    if letra == "2":
        print("costa")
    if letra == "3":
        print("sierra")
    if letra == "4":
        print("selva")
#fin_iterador

print("Fin del bucle")
