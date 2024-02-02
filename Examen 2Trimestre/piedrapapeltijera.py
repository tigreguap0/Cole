import random

def obtener_jugada_usuario():
    while True:
        jugada = input("Elige piedra, papel o tijera: ").lower()
        if jugada == 'piedra' or jugada == 'papel' or jugada == 'tijera':
            return jugada
        else:
            print("Por favor, elige una opción válida.")

def obtener_jugada_computadora():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif (jugada_usuario == 'piedra' and jugada_computadora == 'tijera') or \
         (jugada_usuario == 'papel' and jugada_computadora == 'piedra') or \
         (jugada_usuario == 'tijera' and jugada_computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def main():
    print("Bienvenido al juego de piedra, papel, tijera")

    while True:
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()

        print("La computadora eligió:", jugada_computadora)

        resultado = determinar_ganador(jugada_usuario, jugada_computadora)
        print(resultado)

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            break

    print("Gracias por jugar!")

if __name__ == "__main__":
    main()
