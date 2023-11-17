import random
respuesta = 0
intentos = 0
valor = random.randrange(1, 1000)
while valor != respuesta:
    respuesta = int(input("Introduce 1 numero entre 1 y 1000: "))
    if valor < respuesta:
        print("El valor es mas pequeño")
    if valor > respuesta:
        print("El valor el mayor")
    if valor == respuesta:
        print("Encertaste ole tu!!, lo hiciste en estos intentos: ", intentos)
    intentos = intentos + 1
