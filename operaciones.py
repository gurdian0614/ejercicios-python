n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

if n2 == 0:
    print("Segundo valor no puede ser igual a 0")
else:
    division = str(n1 / n2)
    suma = str(n1 + n2)
    resta = str(n1 - n2)
    multiplicacion = str(n1 * n2)

    print("La suma es: " + suma)
    print("La resta es: " + resta)
    print("La multiplicacion es: " + multiplicacion)
    print("La division es: " + division)