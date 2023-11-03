total_pares = 0
total_impares = 0


for numero in range(1, 51):
    if numero % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1

print("El total de pares es:", total_pares)
print("El total de impares es:", total_impares)
