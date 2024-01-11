import random

def calcular_puntuacion(intentos):
    return 8 - intentos + 1 if intentos <= 8 else 0

def main():
    continuar = True
    puntuaciones = []

    while continuar:
        lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']
        print("Estas son las palabras que puede haber: ", lista)
        valor_al_azar = random.choice(lista)
        intentos = 0

        while True:
            comprobacion = input("Introduce la palabra secreta: ")
            intentos += 1

            if comprobacion == valor_al_azar:
                print(f"¡Acertaste en {intentos} intentos!")
                puntuacion_partida = calcular_puntuacion(intentos)
                puntuaciones.append(puntuacion_partida)
                print(f"Tu puntuación en esta partida ha sido de {puntuacion_partida}")
                break
            else:
                print("Sigue jugando")

        respuesta = input("¿Quieres jugar otra partida? (s/n): ")
        if respuesta.lower() != 's':
            continuar = False

    total_puntuacion = sum(puntuaciones)
    media_puntuacion = total_puntuacion / len(puntuaciones) if len(puntuaciones) > 0 else 0

    print(f"Puntuación {puntuaciones}")
    print(f"Tu puntuación total ha sido de {total_puntuacion}")
    print(f"La media de las partidas realizadas es: {media_puntuacion}")

    if media_puntuacion > 12.0:
        print("¡Tienes buena suerte!")
    else:
        print("Mejor dedícate al parchís")

if __name__ == "__main__":
    main()
