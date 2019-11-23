import os
#DECLARAR VARIABLES
fuerza, area=0, 0

#imput
fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])


#procesing
presion=(fuerza/area)

#Verificador
presion=( presion < 100 or presion > 600 )

#VALIDAR LA PRESRION QUE EJERCE UN BARCO SOBRE UN LAGO
presion_invalida=True
while (presion_invalida):
    presion=int(input("ingrese presion:"))
    presion_invalida=(presion < 100 or presion > 600)
#fin_while
print("fin del bucle")
