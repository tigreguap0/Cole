letras = []

while True:
    letra = input("Introduce una letra: ").lower()

    if letra not in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù']:
        if letra not in letras:
            letras.append(letra)

    repetir = input("¿Deseas repetir? (s/n): ").lower()

    if repetir != 's':
        break

print(letras)
