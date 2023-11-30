

import random

valores_cartas = {
    "Rey♦ (10)": 10, "Reina♦ (10)": 10, "Jota♦ (10)": 10, "Diez♦ (10)": 10, "Nueve♦ (9)": 9, "Ocho♦ (8)": 8, "Siete♦ (7)": 7,
    "Seis♦ (6)": 6, "Cinco♦ (5)": 5, "Cuatro♦ (4)": 4, "Tres♦ (3)": 3, "Dos♦ (2)": 2, "As♦ (1, 11)": (1, 11),
    "Rey♥ (10)": 10, "Reina♥ (10)": 10, "Jota♥ (10)": 10, "Diez♥ (10)": 10, "Nueve♥ (9)": 9, "Ocho♥ (8)": 8, "Siete♥ (7)": 7,
    "Seis♥ (6)": 6, "Cinco♥ (5)": 5, "Cuatro♥ (4)": 4, "Tres♥ (3)": 3, "Dos♥ (2)": 2, "As♥ (1, 11)": (1, 11),
    "Rey♠ (10)": 10, "Reina♠ (10)": 10, "Jota♠ (10)": 10, "Diez♠ (10)": 10, "Nueve♠ (9)": 9, "Ocho♠ (8)": 8, "Siete♠ (7)": 7,
    "Seis♠ (6)": 6, "Cinco♠ (5)": 5, "Cuatro♠ (4)": 4, "Tres♠ (3)": 3, "Dos♠ (2)": 2, "As♠ (1, 11)": (1, 11),
    "Rey♣ (10)": 10, "Reina♣ (10)": 10, "Jota♣ (10)": 10, "Diez♣ (10)": 10, "Nueve♣ (9)": 9, "Ocho♣ (8)": 8, "Siete♣ (7)": 7,
    "Seis♣(6)": 6, "Cinco♣ (5)": 5, "Cuatro♣ (4)": 4, "Tres♣ (3)": 3, "Dos♣ (2)": 2, "As♣ (1, 11)": (1, 11),
}


listacartas = list(valores_cartas.keys()) * 4

def asignar_valor(cartas):
    valor = sum(valores_cartas[carta] if type(valores_cartas[carta]) == int else max(valores_cartas[carta]) for carta in cartas)
    if "As" in cartas and valor + 10 <= 21:
        valor += 10
    return valor

def guardar_resultados(nombre, dinero_ingresado, dinero_apostado, dinero_ganado):
    with open(r"C:\Users\FalomirSerbanMiguel\Documents\GitHub\Cole\Proyecto BlackJack\top.txt", "a") as f:
        f.write(f"Nombre: {nombre}, Dinero Ingresado: {dinero_ingresado}, Dinero Apostado: {dinero_apostado}, Dinero Ganado: {dinero_ganado}\n")

def obtener_cantidad_dinero():
    while True:
        try:
            dinero = float(input("Ingresa la cantidad de dinero que deseas jugar: "))
            return dinero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def obtener_apuesta_actual(dinero_actual):
    while True:
        try:
            apuesta = float(input("¿Cuánto deseas apostar?: "))
            if apuesta <= dinero_actual:
                return apuesta
            else:
                print("No puedes apostar más dinero del que tienes. Introduce una apuesta válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def jugar_blackjack():
    nombre_jugador = input("Ingresa tu nombre: ")
    dinero_ingresado = obtener_cantidad_dinero()
    dinero_actual = dinero_ingresado

    while dinero_actual > 0:
        print(f"Dinero actual: {dinero_actual}")
        apuesta_actual = obtener_apuesta_actual(dinero_actual)

        random.shuffle(listacartas)

        mano_jugador = [listacartas.pop(), listacartas.pop()]
        mano_banca = [listacartas.pop(), listacartas.pop()]

        while True:
            print(f"Mano del jugador: {mano_jugador}, Valor: {asignar_valor(mano_jugador)}")
            print(f"Primera carta de la banca: {mano_banca[0]}")

            if asignar_valor(mano_jugador) == 21:
                print("¡Blackjack! ¡Ganaste!")
                dinero_actual += apuesta_actual
                break

            accion = input("¿Quieres pedir otra carta? (s/n): ").lower()

            if accion == 's':
                nueva_carta = listacartas.pop()
                mano_jugador.append(nueva_carta)
                print(f"Has recibido una carta: {nueva_carta}")

                if asignar_valor(mano_jugador) > 21:
                    print("Te has pasado de 21. ¡Has perdido!")
                    dinero_actual -= apuesta_actual
                    break
            else:
                while asignar_valor(mano_banca) < 17:
                    carta_banca = listacartas.pop()
                    mano_banca.append(carta_banca)
                    print(f"La banca ha recibido una carta: {carta_banca}")

                print(f"Mano del jugador: {mano_jugador}, Valor TOTAL:    {asignar_valor(mano_jugador)}")
                print(f"Mano de la banca: {mano_banca}, Valor TOTAL:    {asignar_valor(mano_banca)}")

                if asignar_valor(mano_banca) > 21:
                    print("La banca se ha pasado de 21. ¡Ganaste!")
                    dinero_actual += apuesta_actual
                    break
                elif asignar_valor(mano_jugador) > asignar_valor(mano_banca):
                    print("¡Ganaste!")
                    dinero_actual += apuesta_actual
                    break
                elif asignar_valor(mano_jugador) < asignar_valor(mano_banca):
                    print("¡Perdiste!")
                    dinero_actual -= apuesta_actual
                    break
                else:
                    print("Empate. Nadie gana.")
                    break

        print(f"Dinero ganado: {dinero_actual - dinero_ingresado}")
        print(f"Dinero perdido: {dinero_ingresado - dinero_actual}")

        # Guardar resultados en el archivo top.txt
        guardar_resultados(nombre_jugador, dinero_ingresado, apuesta_actual, dinero_actual - dinero_ingresado)

        jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print("Gracias por jugar. ¡Hasta luego!")

jugar_blackjack()
