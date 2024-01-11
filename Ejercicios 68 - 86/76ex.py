lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

letras = [elemento for elemento in lista1 if elemento.isalpha()]
numeros = [int(elemento) for elemento in lista1 if elemento.isdigit()]

orden = int(input("Introduce 1 para visualizar en orden ascendente o 2 para descendente: "))

if orden == 1:
    letras.sort(key=str.casefold)
    numeros.sort()
else:
    letras.sort(key=str.casefold, reverse=True)
    numeros.sort(reverse=True)

print(numeros)
print(letras)
