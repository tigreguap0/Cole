total_pares = 0
total_impares = 0
total_positivos = 0
total_negativos = 0
total_ceros = 0
suma_total = 0

while True:
    numero = int(input("Introduce un número: "))

    if numero == -99:
        break

    if numero % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1

    if numero > 0:
        total_positivos += 1
    elif numero < 0:
        total_negativos += 1
    else:
        total_ceros += 1

    suma_total += numero

# Mostramos el resumen
print("RESUMEN")
print("El número de pares es", total_pares)
print("El número de impares es", total_impares)
print("El número de positivos es", total_positivos)
print("El número de negativos es", total_negativos)
print("El total es", suma_total)
