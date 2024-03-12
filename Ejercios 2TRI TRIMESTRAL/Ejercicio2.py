
# A B C D E F G


import random
import time

def multiplicacion(numeros):
    aciertos = []
    fallos = []

    num_multiplicaciones = int(input("¿Cuantas multiplicaciones quieres resolver? "))
    print("CALCULANDO...")
    time.sleep(0.5)
    for _ in range(num_multiplicaciones):
        num1 = random.randint(numeros[0], numeros[1])
        num2 = random.randint(numeros[0], numeros[1])

        respuesta = input(f"¿Cuánto es {num1} x {num2}? (Responde 'F' para salir): ")

        if respuesta.upper() == 'F':
            break

        try:
            respuesta_usuario = int(respuesta)
            producto = num1 * num2

            if respuesta_usuario == producto:
                
                aciertos.append((num1, num2, respuesta_usuario))
                print("Verificando...")
                time.sleep(0.4)
                print("¡Respuesta correcta!")
            else:
                fallos.append((num1, num2, respuesta_usuario, producto))
                print("Verificando...")
                time.sleep(0.4)
                print("Respuesta incorrecta. El resultado es", producto)
        except ValueError:
            print("Respuesta no válida. Introduce un numero o 'F' para salir.")

    total_preguntas = len(aciertos) + len(fallos)
    if total_preguntas > 0:
        porcentaje_aciertos = (len(aciertos) / total_preguntas) * 100
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f} % ")
    else:
        print("No se realizaron preguntas.")

    print("\nAciertos:")
    for acierto in aciertos:
        print(f"{acierto[0]} x {acierto[1]} = {acierto[2]}")

    print("\nFallos:")
    for fallo in fallos:
        print(f"{fallo[0]} x {fallo[1]} = {fallo[3]} (Respuesta del usuario: {fallo[2]})")

minimo = int(input("Introduce el numero minimo para las multiplicaciones: "))

time.sleep(0.2)
print("calculando.")
time.sleep(0.2)
print("calculando..")
time.sleep(0.2)
print("calculando...")

maximo = int(input("Introduce el numero maximo para las multiplicaciones: "))

time.sleep(0.2)
print("calculando...")
time.sleep(0.2)
print("calculando..")
time.sleep(0.2)
print("calculando.")

multiplicacion([minimo, maximo])
