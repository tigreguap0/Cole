def sumar_cifras(numero):
    suma = 0
    for cifra in str(numero):
        suma += int(cifra)
    return suma

num_cifras = int(input("Introduce un número por cifras: "))


num_ingresado = int(input(f"Introduce un número de {len(str(num_cifras))} cifras: "))


while len(str(num_ingresado)) != len(str(num_cifras)):
    print("Error: El número ingresado no tiene la misma cantidad de cifras. Intenta de nuevo.")
    num_ingresado = int(input(f"Introduce un número de {len(str(num_cifras))} cifras: "))

resultado = sumar_cifras(num_ingresado)
print(f"La suma de las cifras es: {resultado}")
