
a = int(input("Introduce el primer intervalo: "))
b = int(input("Introduce el segundo intervalo: "))


if a < b:
    for i in range(a, b + 1):
        print(i, end="-")
else:
    for i in range(a, b - 1, -1):
        print(i, end="-")
print()
