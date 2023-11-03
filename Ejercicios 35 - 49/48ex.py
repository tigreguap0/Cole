palabra_secreta = input("Introduce la palabra secreta: ")
longitud_palabra = len(palabra_secreta)
oportunidades = int(input("Introduce el número de oportunidades: "))

for _ in range(oportunidades):
    letra = input("Introduce una letra: ")
    if letra in palabra_secreta:
        print("La letra existe")
    else:
        print("La letra no existe")

print("Se te han agotado las oportunidades. La palabra secreta era:", palabra_secreta)
