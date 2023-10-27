import time
import math

pregunta = "s"
mensaje_error = ""

while pregunta == "s":
    print("Instrucciones")
    time.sleep(0.3)
    print("1. La longitud de la contraseña debe tener entre 6 y 8 caracteres")
    time.sleep(0.3)
    print("2. Forzaremos los siguientes valores según su posición indicada")
    time.sleep(0.3)
    print("---> Posición 1: Un número mayor o igual a 1 y menor o igual que 5")
    time.sleep(0.3)
    print("---> Posición 2: Una letra minúscula")
    time.sleep(0.3)
    print("---> Posición 3: Una letra mayúscula")
    time.sleep(0.3)
    print("---> Posición 4: Uno de los siguientes símbolos: *, _, @")
    time.sleep(0.3)
    print("---> Posición 5: Una letra minúscula")
    time.sleep(0.3)
    print("---> Posición 6: Un número mayor o igual a 6 y menor o igual que 9")
    time.sleep(0.3)
    print("---> Posición 7: Uno de los siguientes símbolos: &, /, #")
    time.sleep(0.3)
    print("---> Posición 8: Un número menor o igual que 5")
    time.sleep(0.3)



    password = input("Introduce la contraseña: ")

    # Longitud de la contraseña
    longitud = len(password)

    #####################
    v1 = 0
    v2 = []
    #####################

    # Verificación de la longitud de la contraseña
    if 6 <= longitud <= 8:
        print("La longitud de la contraseña es correcta")
    else:
        print("Error, el password tiene una longitud de " + str(longitud) + " caracteres y no cumple los requisitos")
        exit()

    posicion6 = password[5]

    # Verificación de las posiciones
    if 1 <= int(password[0]) <= 5:
        v1 = (v1 + 1)
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 1 ")

    if password[1].islower():
        v1 = (v1 + 1)
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 2 ")

    if password[2].isupper():
        v1 = (v1 + 1)
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 3 ")

    if password[3] in ('*', '_', '@'):
        v1 = (v1 + 1)
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 4 ")

    if password[4].islower():
        v1 = (v1 + 1)
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 5 ")

    if posicion6.isnumeric():
        if longitud >= 6:
            if int(password[5]) >= 6 and int(password[5]) <= 9:
                v1 = (v1 + 1)
            else:
                mensaje_error= (mensaje_error + "Error en el carácter 6 ")
    else:
        mensaje_error= (mensaje_error + "Error en el carácter 6 ")

    if longitud >= 7:
        if password[6] in ('&', '/', '#'):
            v1 = (v1 + 1)
        else:
            mensaje_error= (mensaje_error + "Error en el carácter 7 ")

    if longitud == 8:
        if int(password[7]) <= 5:
            v1 = (v1 + 1)
        else:
            mensaje_error= (mensaje_error + "Error en el carácter 8 ")

    # Saber la cantidad de errores
    if v1 == longitud:
        print("El formato del PASSWORD es correcto") 
    else:
        print("Tiene los siguientes errores:")
        print(mensaje_error)
    pregunta = input("¿Deseas repetir el programa? s / n:   ")
else:
    print("Fin del programa")