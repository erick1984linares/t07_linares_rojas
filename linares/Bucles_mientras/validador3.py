import os
#DECLARAR VARIABLES
masa, aceleracion=0, 0

#imput
masa=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])

#procesing
fuerza=(masa*aceleracion)

#Verificador
fuerza=(fuerza < 500 or fuerza > 1500 )

#VALIDAR LA FUERZA NECESARIA DE UNA MAQUINA DE CONSTRUIR EDIFICIOS
fuerza_invalida=True
while (fuerza_invalida):
    fuerza=int(input("ingrese fuerza:"))
    fuerza_invalida=(fuerza < 500 or fuerza > 1500)
#fin_while
print("fin del bucle")
