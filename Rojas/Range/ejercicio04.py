import os
#mostrar los numeros  de 1 hasta p sumados mas 3
x=int(os.sys.argv[1])
p=int(os.sys.argv[2])

for x in range (p):
    print(x+3)
    x+=2


#Fin_iterador_rango
print("fin del bucle")
