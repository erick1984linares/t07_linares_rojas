import os
#DECLARAR VARIABLES
distancia, tiempo=0, 0

#imput
distancia=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])


#procesing
velocidad=(distancia/tiempo)

#Verificador
velocidad=(velocidad < 10 or velocidad > 35 )

#VALIDAR LA VELOCIDAD
velocidad_invalida=True
while (velocidad_invalida):
    velocidad=int(input("ingrese velocidad:"))
    velocidad_invalida=(velocidad < 10 or velocidad > 35)
#fin_while
print("fin del bucle")
