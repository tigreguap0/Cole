import random

pregunta_elegida = random.randint(1, 10) 

Respuesta1 = input("Escoge un numero del 1 al 10: ")


Respuesta1 = int(Respuesta1)

if Respuesta1 == pregunta_elegida:
    print("Respuesta correcta")
else:
    print("Respuesta incorrecta la respuesta correcta era: ", pregunta_elegida)

