import os
#DECLARAR VARIABLES
pi, radio, generatriz=0, 0, 0

#imput
pi=float(os.sys.argv[1])
radio=int(os.sys.argv[2])
generatriz=int(os.sys.argv[3])

#procesing
volumen_de_un_cilindro=(pi*radio*radio*generatriz)

#Verificador
volumen=(volumen < 18.5 or volumen > 64.6 )

#VALIDAR EL VOLUMEN DE UN CILINDRO
volumen_invalido=True
while (volumen_invalido):
    volumen=int(input("ingrese volumen del cilindro:"))
    volumen_invalido=(volumen < 18.5 or volumen > 64.6  )
#fin_while
print("fin del bucle")
