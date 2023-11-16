repeticiones = 0
resultados = 0

while resultados <= 50:
    v1 = int(input("Dime tu primer numero: "))
    v2 = int(input("Dime tu segundo numero: "))
    resultado = v1 + v2
    repeticiones += 1
    resultados += resultado
    print("Resultado de la operación:", resultado)

if repeticiones == 1:
    print("El total acumulado es:", resultados, "y has realizado", repeticiones, "operación.")
elif repeticiones > 1:
    print("El total acumulado es:", resultados, "y has realizado", repeticiones, "operaciones.")
else:
    print("No has realizado ninguna operación.")
