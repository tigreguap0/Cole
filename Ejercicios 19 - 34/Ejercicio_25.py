v1 = float(input("Introduce la nota del examen: "))

if v1 < 0 or v1 > 10:
    print("Introduce un numero entre o y 10")

elif v1 < 0 or v1 < 5:
    print("Sacaste un insuficiente")

elif v1 < 5 or v1 < 6.4:
    print("suficiente")

elif v1 < 6.5 or v1 < 8.4:
    print("Notable")

elif v1 < 8.5 or v1 < 10:
    print("Excelente")
