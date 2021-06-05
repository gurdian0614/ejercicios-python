# Funcion que me calcule el isv
# 15% ventas
# 18% alcohol, tabaco
# usuario debe definir el valor del isv a calcular
# tipo: 1. 15%, 2. 18%

def isv(valor, tipo):
    if tipo == 1:
        return valor * 0.15
    elif tipo == 2:
        return valor * 0.18
    else:
        return -1

def menu():
    print("*********************************")
    print("*              MENU             *")
    print("* 1. Calcular 15%               *")
    print("* 2. Calcular 18%               *")
    print("* 3. Salir                      *")
    print("*********************************")
    opcion = int(input("Escoja la opcion: "))
    return opcion

opcion = menu()
while opcion != 3:
    if opcion == 1 or opcion == 2:
        valor = int(input("Ingrese Valor Neto: "))
        calculo = isv(valor, opcion)
        print("ISV: " + str(calculo) + "\n")
    else:
        print("Opcion no valida\n")

    opcion = menu()