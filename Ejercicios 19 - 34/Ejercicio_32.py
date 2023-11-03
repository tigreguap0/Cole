frase = "A quién madruga Dios ayuda"
print("*****FRASE*****")
print(frase)
print("*****FRASE*****")


palabra = input("Introduce una palabra de la frase de arriba: ")


frase_minuscula = frase.lower()
palabra_minuscula = palabra.lower()


if palabra_minuscula in frase_minuscula:
    
    posicion = frase_minuscula.index(palabra_minuscula)
    print(f"La palabra '{palabra}' está en la posición {posicion} en la frase original.")
else:
    print(f"La palabra '{palabra}' no está en la frase.")
