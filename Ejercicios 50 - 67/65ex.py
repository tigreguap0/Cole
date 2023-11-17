numeros_ingresados = False

while True:
    entrada = input("Introduce un número (o -99 para salir): ")

    if entrada == "-99":
        break

    numero = float(entrada)

    if not numeros_ingresados:
        maximo = numero
        minimo = numero
        numeros_ingresados = True
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

if numeros_ingresados:
    print(f"El número máximo es: {maximo}")
    print(f"El número mínimo es: {minimo}")
else:
    print("No se introdujeron números.")
