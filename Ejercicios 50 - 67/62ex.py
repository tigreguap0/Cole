
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))


if inicio > fin:
    inicio, fin = fin, inicio


pares = []
impares = []


for num in range(inicio, fin + 1):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)


print("Los números pares son:", end=" ")
for par in pares:
    print(par, end="-")
print()

print("Los números impares son:", end=" ")
for impar in impares:
    print(impar, end="-")
print()

