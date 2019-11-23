import os
# validar la edad del usuario mayor de edad
edad=int(os.sys.argv[1])
print(edad)
edad_invalida=True


while (edad_invalida):
    print("####################################################")
    print("#Ingrese edad del usuario (mayor de edad):", edad,"#")
    print("####################################################")
    edad_invalida = (edad < 17 or edad > 100)
    if (edad_invalida):
        print("<< la edad es invalida >>")
    else:
        print("<< edad correcta >>")

#Fin_while
print("Fin del bucle")
