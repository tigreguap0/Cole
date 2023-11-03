v1 = float(input("Introduce la nota del examen: "))

if v1 < 0 or v1 > 10:
    print("Introduce un numero entre o y 10")

elif v1 > 5:
    print("aprobaste")

elif v1 < 5:
    print("suspendiste")

