v1 = int(input("Introduce la nota del examen: "))

if v1 < 0 or v1 > 10:
    print("Error, introduce un número entre 0 y 10")
elif v1 < 5:
    print("Has suspendido, chaval. Estudia más.")
else:
    print("¡Ole tú, chaval! Has aprobado. Sigue así.")

input()
