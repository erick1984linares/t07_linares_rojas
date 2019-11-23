import os
#mostrar error mientras la clave de acceso no sea 2019
clave=int(os.sys.argv[1])
invalida=True

while(invalida):
    print("##################################")
    print("Ingrese la clave de acceso:", clave)
    print("##################################")
    invalida=(clave != 2019)
    if (invalida == True):
        print("<< error >>")
    else:
        print("<< correcto >>")

#fin_bucle
print("fin del bucle")
