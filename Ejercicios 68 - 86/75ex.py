lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

cantidad_total = len(lista1)

cantidad_numeros = 0
for elemento in lista1:
    if elemento.isdigit():
        cantidad_numeros += 1

cantidad_letras = 0
for elemento in lista1:
    if elemento.isalpha():
        cantidad_letras += 1

cantidad_mayusculas = 0
for elemento in lista1:
    if elemento.isupper():
        cantidad_mayusculas += 1

suma_numeros = 0
for elemento in lista1:
    if elemento.isdigit():
        suma_numeros += int(elemento)

print("Número de valores:", cantidad_total)
print("Cantidad de números:", cantidad_numeros)
print("Cantidad de letras:", cantidad_letras)
print("Cantidad de mayúsculas:", cantidad_mayusculas)
print("Suma total de números:", suma_numeros)
