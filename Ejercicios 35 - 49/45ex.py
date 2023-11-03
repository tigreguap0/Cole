
palabra = input("Introduce una palabra: ")

vocales = []
consonantes = []

for letra in palabra:
    if letra.lower() in "aeiou":
        vocales.append(letra)
    else:
        consonantes.append(letra)

print("Las vocales de la palabra", palabra, "son:", "".join(vocales))
print("Las consonantes de la palabra", palabra, "son:", "".join(consonantes))
