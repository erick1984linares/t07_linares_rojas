import os
#Mostrar error mientras la nota ingresada sea invalida
nota=int(os.sys.argv[1])
nota_erronea=True

while(nota_erronea):
    print("############################")
    print("Ingrese la nota obtenida:",nota)
    print("############################")
    nota_erronea=(nota>20 or nota<0)
    if (nota == True):
        print("nota incorrecta")
    else:
        print("nota correcta")
#Fin_while
print("Fin del bucle")
