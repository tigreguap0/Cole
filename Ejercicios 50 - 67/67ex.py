password = input("Introduce la contraseña: ")
repetir = "s"
while repetir == "s":
    if 8 <= len(password) <= 10:
        num_digitos_1_5 = 0
        num_digitos_6_8 = 0
        num_letras_minusculas = 0
        num_letras_mayusculas = 0
        num_simbolos = 0

        for caracter in password:
            if caracter.isdigit():
                if 1 <= int(caracter) <= 5:
                    num_digitos_1_5 += 1
                elif 6 <= int(caracter) <= 8:
                    num_digitos_6_8 += 1
            elif caracter.islower():
                num_letras_minusculas += 1
            elif caracter.isupper():
                num_letras_mayusculas += 1
            elif caracter in ['*', '_', '@', '&', '/', '#']:
                num_simbolos += 1

        if (
            num_digitos_1_5 >= 2
            and num_digitos_6_8 >= 1
            and num_letras_minusculas >= 2
            and num_letras_mayusculas >= 1
            and num_simbolos >= 2
        ):
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
    else:
        print("Contraseña incorrecta")
    repetir = input("Deseas repetir el programa s / n: ")
