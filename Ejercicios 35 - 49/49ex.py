palabra_secreta = input("Introduce la palabra secreta: ")
longitud_palabra = len(palabra_secreta)
oportunidades = int(input("Introduce el número de oportunidades: "))

for _ in range(oportunidades):
    letra = input("Introduce una letra: ")
    if letra in palabra_secreta:
        posiciones = [str(i) for i, c in enumerate(palabra_secreta) if c == letra]
        if posiciones:
            print("La letra se encuentra en la posición(es):", ", ".join(posiciones))
        else:
            print("La letra no existe en la palabra secreta.")
    else:
        print("La letra no existe en la palabra secreta.")

print("Se te han agotado las oportunidades. La palabra secreta era:", palabra_secreta)
