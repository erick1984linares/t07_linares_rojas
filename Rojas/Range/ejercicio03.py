import os
#mostrar los numeros  de 1 hasta n multiplicados por 10
x=int(os.sys.argv[1])
n=int(os.sys.argv[2])

for x in range (n):
    print(x*10)
    x+=2


#Fin_iterador_rango
print("fin del bucle")
