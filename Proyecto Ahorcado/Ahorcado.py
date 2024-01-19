import random
import time

def cargar_palabras_desde_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read().splitlines()

def iniciar_partida():
    ruta_archivo_palabras = r'C:\\Users\\FalomirSerbanMiguel\Documents\\GitHub\\Cole\\Proyecto Ahorcado\\palabras.txt'
    Lista_palabrasecreta = cargar_palabras_desde_archivo(ruta_archivo_palabras)
    
    if not Lista_palabrasecreta:
        print("Error: No hay palabras en el archivo. Añade palabras antes de jugar.")
        return

    palabra_secreta = random.choice(Lista_palabrasecreta)
    Lista_partida = ["_"] * len(palabra_secreta)
    Lista_ahorcado = []
    Lista_aciertos = []
    Lista_errores = []
    
    intentos_fallidos = 0
    tiempo_inicio = time.time()

    while intentos_fallidos < 8:
        print("Palabra actual: ", " ".join(Lista_partida))
        print("Letras incorrectas: ", " ".join(Lista_errores))
        print("Ahorcado: ", " ".join(Lista_ahorcado))

        letra = input("Introduce una letra: ").lower()

        if letra in Lista_aciertos or letra in Lista_errores:
            print("Ya has ingresado esa letra. Intenta de nuevo.")
            continue

        if letra in palabra_secreta:
            for palabra in range(len(palabra_secreta)):
                if palabra_secreta[palabra] == letra:
                    Lista_partida[palabra] = letra
                    Lista_aciertos.append(letra)
        else:
            intentos_fallidos += 1
            Lista_errores.append(letra)
            Lista_ahorcado.append("A H O R C A D O"[intentos_fallidos - 1])

        if "_" not in Lista_partida:
            tiempo_fin = time.time()
            duracion = tiempo_fin - tiempo_inicio
            print("¡Enhorabuena! Has adivinado la palabra:", palabra_secreta)
            print("Número de errores:", intentos_fallidos)
            print("Número de aciertos:", len(Lista_aciertos))
            print("Tiempo de juego: {} minutos y {:.2f} segundos".format(int(duracion // 60), duracion % 60))
            break

    else:
        print("Lo siento, has alcanzado el límite de intentos. La palabra secreta era:", palabra_secreta)
        print("Número de errores:", intentos_fallidos)
        print("Número de aciertos:", len(Lista_aciertos))


while True:
    iniciar_partida()

    continuar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if continuar != 's':
        quit


