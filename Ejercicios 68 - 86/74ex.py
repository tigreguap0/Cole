palabras = []
lista1 = ['casa', 'mesa', 'sal', 'sol', 'agua']

while True:
    palabra = input("Introduce una palabra: ").lower()

    if palabra not in lista1 and palabra not in palabras:
        palabras.append(palabra)

    repetir = input("¿Deseas repetir? (s/n): ").lower()
    if repetir != 's':
        break

repetidas = [palabra for palabra in lista1 if palabra in palabras]
no_repetidas = [palabra for palabra in palabras if palabra not in lista1]

print(f"Están repetidas: {repetidas}")
print(f"No están repetidas: {no_repetidas}")
