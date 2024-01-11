
lista1 = []
lista2 = []

num_palabras = int(input("Introduce la cantidad de palabras: "))

for i in range(1, num_palabras + 1):
    palabra = input(f"Introduce {i}ª palabra: ")
    lista1.append(palabra)

lista2 = lista1.copy()
lista2.reverse()

print("lista1 contiene:", lista1)
print("lista2 contiene:", lista2)
