import random
i = 0
v1 = random.randrange(1, 5)
while i != 3:
    respuesta = int(input("Introduce un numero del 1 al 5: "))
    if respuesta == v1:
        print("Respuesta correcta")
        exit()
    else:
        print("La respuesta es incorrecta pero tienes otra oportunidad. ")
    i = i + 1