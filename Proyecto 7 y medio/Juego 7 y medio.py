import random

def obtener_carta():
    """Obtiene una carta al azar."""
    carta = random.randint(1, 12)
    if carta == 8 or carta == 9:
        return obtener_carta()  
    return carta

def calcular_puntuacion(carta):
    """Calcula la puntuación de una carta."""
    if carta <= 7:
        return carta
    else:
        return 0.5

def jugar_partida():
    puntos = 100  
    while puntos > 0:
        print(f"Puntos disponibles: {puntos}")
        input("Presiona Enter para obtener una carta...")
        carta = obtener_carta()
        puntuacion = calcular_puntuacion(carta)
        puntos += puntuacion
        print(f"Obtuviste una carta con puntuación {puntuacion}. Tu puntuación actual es {puntos}")
        
        if puntos == 7.5:
            print("¡Enhorabuena, has ganado la partida!")
            puntos += 10
        elif puntos > 7.5:
            print("Has perdido la partida!")
            puntos -= 10
        else:
            plantarse = input("¿Quieres plantarte? (S/N): ").strip().lower()
            if plantarse == 's':
                if puntos >= 6:
                    print("Has sido un poco conservador")
                    puntos += 5
                else:
                    print("Quizás tendrías que arriesgar un poco ¿no?")
                    puntos -= 5

        replay = input("¿Quieres jugar otra partida? (S/N): ").strip().lower()
        if replay != 's':
            break

    print(f"Fin del juego. Tu puntuación final es: {puntos}")


