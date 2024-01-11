import random

def desordenar_palabra(palabra):
    lista_letras = list(palabra)
    random.shuffle(lista_letras)
    return ''.join(lista_letras)

lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']

valor_al_azar = random.choice(lista)
palabra_desordenada = desordenar_palabra(valor_al_azar)

print("Palabra desordenada: ", palabra_desordenada)

intentos = 3
for _ in range(intentos):
    intento_usuario = input("Introduce la palabra correcta: ")

    if intento_usuario == valor_al_azar:
        print("¡Acertaste!")
        break
    else:
        print("No has acertado")

if intento_usuario != valor_al_azar:
    print("No has acertado ninguno de los intentos. La palabra correcta era:", valor_al_azar)
