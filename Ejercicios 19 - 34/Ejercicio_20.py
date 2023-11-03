v1 = float(input("Introduce tu primer numero: "))

v2 = float(input("Introduce tu segundo numero: "))

if v1 < 0 or v1 > 10:
    print("Introduce un numero entre o y 10")

if v2 < 0 or v2 > 10:
    print("Introduce un numero entre o y 10")

elif v1 > v2:
    print("El primer numero es mayor")

elif v2 > v1:
    print("El segundo numero es mayor")

else:
    print("Son iguales")