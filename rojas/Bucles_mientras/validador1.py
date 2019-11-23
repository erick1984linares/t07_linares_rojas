import os
#DECLARAR VARIABLES
largo, ancho, altura=0, 0, 0

#imput
largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#procesing
volumen=(largo*ancho*altura)

#VALIDAR EL VOLUMEN DE UN RECTOEDRO
volumen_invalido=True
while (volumen_invalido):
    volumen=int(input("ingrese volumen:"))
    volumen_invalido=(volumen < 24 or volumen > 60  )
#fin_while
print("fin del bucle")
