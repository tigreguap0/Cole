import random
v1 = random.randrange(1, 5)
respuesta = int(input("Introduce un numero del 1 al 5: "))
if respuesta == v1:
    print("Respuesta correcta")
else:
    print("La respuesta es incorrecta el valor era: ",v1)