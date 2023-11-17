import time
veces = 0
valor = 1
pregunta = int(input("Introduce el valor para que te haga la tabla: "))
while veces != 10:
    respuesta = (pregunta * valor)
    time.sleep(0.3)
    print(respuesta)
    valor = valor + 1
    veces = veces + 1