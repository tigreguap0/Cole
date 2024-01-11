
letras = []

while True:
    letra = input("Introduce una letra: ")

    if letra not in letras:
        letras.append(letra)

    repetir = input("¿Deseas repetir? (s/n): ").lower()

    if repetir != 's':
        break

print(letras)
