import os
# Mostrar "Invalido" mientras no se ingrese un curso correcto
curso=os.sys.argv[1]
invalido=True

while(invalido):
    print("##########################################")
    print("Ingrese el curso a consultar:", curso)
    print("##########################################")
    invalido=(curso != "Matematica" and
              curso != "Programacion" and
              curso != "Quimica" and
              curso != "Analisis")
    if (invalido == True):
        print("<< curso invalido >>")
    else:
        print("consultando...")

#fin_while
print("Fin del bucle")
