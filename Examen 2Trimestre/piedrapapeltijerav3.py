import random

total_partidas = 0
victorias_usuario = 0
victorias_IA = 0
empates = 0

def obtener_jugada_usuario():
    while True:
        jugada = input("Elige piedra, papel o tijera: ").lower()
        if jugada in ['piedra', 'papel', 'tijera']:
            return jugada
        else:
            print("Por favor, elige una opción válida.")

def obtener_jugada_IA():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(jugada_usuario, jugada_IA):
    global total_partidas, victorias_usuario, victorias_IA, empates

    total_partidas += 1
    
    if jugada_usuario == jugada_IA:
        empates += 1
        print("Empate menol MAS SUERTE LA PROXMA ^^")
    elif (jugada_usuario == 'piedra' and jugada_IA == 'tijera') or \
         (jugada_usuario == 'papel' and jugada_IA == 'piedra') or \
         (jugada_usuario == 'tijera' and jugada_IA == 'papel'):
        
        victorias_usuario += 1
        print("¡Ganaste, OLE TU ERES GRANDE SIGUE ASI!")
    else:
        victorias_IA += 1
        print("¡LA IA TE HA GANADO XAVALIN!")

def main():
    print("GOOD MORNING USA, OJALA TE GANE LA IA SIEMPRE GANA, PIEDRA PAPEL O TIJERA")
    jugar = True

    while jugar:
        jugada_usuario = obtener_jugada_usuario()
        jugada_IA = obtener_jugada_IA()

        print("La IA eligio:", jugada_IA)

        determinar_ganador(jugada_usuario, jugada_IA)

        respuesta = input("¿Quieres jugar de nuevo? (s/n): ")
        if respuesta.lower() != 's':
            jugar = False

    porcentaje_victorias_usuario = (victorias_usuario / total_partidas) * 100 if total_partidas > 0 else 0
    porcentaje_victorias_IA = (victorias_IA / total_partidas) * 100 if total_partidas > 0 else 0
    porcentaje_empates = (empates / total_partidas) * 100 if total_partidas > 0 else 0

    print("Estadisticas:")
    print("Numero total de partidas:", total_partidas)
    print("Porcentaje de victorias del usuario:", porcentaje_victorias_usuario, "%")
    print("Porcentaje de victorias de la IA:", porcentaje_victorias_IA, "%")
    print("Porcentaje de empates:", porcentaje_empates, "%")

    print("Gracias por jugar!")

if __name__ == "__main__":
    main()
