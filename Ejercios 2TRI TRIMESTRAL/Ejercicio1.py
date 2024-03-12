import random

multiplicaciones = []
for i in range(10):
    factor1 = random.randint(0, 10)
    factor2 = random.randint(0, 10)
    multiplicaciones.append((factor1, factor2))

aciertos = 0
respuestas_alumno = []
for multiplicacion in multiplicaciones:
    factor1, factor2 = multiplicacion
    print(f"{factor1} x {factor2} = ?")
    respuesta_alumno = int(input())
    respuestas_alumno.append(respuesta_alumno)

    respuesta_correcta = factor1 * factor2
    if respuesta_alumno == respuesta_correcta:
        print("Correcto")
        aciertos += 1
    else:
        print("Error")

print(f"Has conseguido {aciertos} puntos.")

print("Las respuestas correctas eran:")
print(respuestas_alumno)
