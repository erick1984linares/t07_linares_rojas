# Decodificar mensaje encriptado
# 1 = ¿donde estas?
# 2 = ya llego el profesor
# 3 = Hizo mucha clase
# 4 = Ven rapido
import os
#input
msg=os.sys.argv[1].upper()
#bucle
for letra in msg:
    if letra == "1":
        print("¿donde estas?")
    if letra == "2":
        print("ya llego el profesor")
    if letra == "3":
        print("hizo mucha clase")
    if letra == "4":
        print("ven rapido")
#fin_iterador
print("...")
print("Fin del bucle")
