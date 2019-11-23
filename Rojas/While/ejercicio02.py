import os
#Mientras el numero ingresado no sea natural mostar mensaje
x=int(os.sys.argv[1])
i=0
invalid=True

while (invalid):
    print("###############################")
    print("Ingrese un numero natural:", x)
    print("###############################")
    invalid=(x<0)
    if (invalid == True):
        print("<< numero incorrecto >>")
    else:
        print("<< numero correcto >>")
#Fin_while
print("Fin del bucle")
