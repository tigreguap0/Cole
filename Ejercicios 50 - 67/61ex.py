import time
veces = 0
valor = 1
respuesta = 0
pregunta = int(input("Introduce el valor para que te haga la tabla: "))
while respuesta < 40:
    respuesta = (pregunta * valor)
    time.sleep(0.3)
    print(respuesta)
    valor = valor + 1
    veces = veces + 1
print("fin del programa")