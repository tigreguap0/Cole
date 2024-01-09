palabras = []

while True:
    palabra = input("Introduce una palabra: ").lower()

    if palabra not in ['casa', 'mesa', "sal", 'sol', 'agua']:
        if palabra not in palabras:
            palabras.append(palabra)

    repetir = input("¿Deseas repetir? (s/n): ").lower()

    if repetir != 's':
        break

print(palabras)
