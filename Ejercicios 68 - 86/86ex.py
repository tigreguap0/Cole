LISTA_DNI_CORRECTOS_MENOS_A_MAS = []
LISTA_DNI_INCORRECTOS_MENOS_A_MAS = []
LISTA_TOTAL_DE_ERRORES = []
NUMERO_TOTAL_DNI_CORRECTO = 0 
PORCIENTO_DNI_CORRECTOS = 0.0  
PORCIENTO_DNI_INCORRECTOS = 0.0  
PORCIENTO_ERROR_LONGITUD = 0.0 
PORCIENTO_ERROR_NUMEROS = 0.0  
PORCIENTO_NO_EXISTENTES = 0.0  
error = 0

def calcular_letra_dni(numero):
    global error  
    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    try:
        if len(numero) == 8 and numero.isdigit():
            numero = int(numero)
            resto = numero % 23
            letra = tabla_letras[resto]
            dni_completo = f"{numero}-{letra}"
            print(f"NIF completo: {dni_completo}")

            if letra not in tabla_letras:
                print("Error: Resto incorrecto, no se encuentra en la tabla.")
                error += 1
                return 2
            else:
                return 3

        else:
            print("Error: El número debe tener 8 dígitos y ser numérico.")
            error += 1
            return 1
    except ValueError:
        print("Error: Introduce un número válido.")
        return 0

LISTA_INTENTOS = []
LISTA_DNI_CORRECTOS = []
LISTA_DNI_INCORRECTOS = []

while True:
    numero_dni = input("Introduce un número de DNI de 8 dígitos: ")
    codigo_resultado = calcular_letra_dni(numero_dni)

    LISTA_INTENTOS.append(codigo_resultado)

    if codigo_resultado == 3:
        NUMERO_TOTAL_DNI_CORRECTO += 1
        LISTA_DNI_CORRECTOS.append(numero_dni)
    else:
        LISTA_DNI_INCORRECTOS.append(numero_dni)

    continuar = input("¿Desea realizar otro cálculo? (s/n): ").lower()
    if continuar != "s":
        print("MENÚ del apartado 7.")
        break

print("1. Listar DNI correctos ordenados de menor a mayor")
print("2. Listar DNI incorrectos ordenados de menor a mayor")
print("3. Número total de errores")
print("4. Número total de DNIs correctos")
print("5. PORCNETAJE de DNI correctos, incorrectos, errores de longitud, errores de número, no existentes.")
print("6. REPETIR PROGRAMA")

opcion = int(input("Introduce un número: "))

if opcion == 1:
    LISTA_DNI_CORRECTOS_MENOS_A_MAS = sorted(LISTA_DNI_CORRECTOS)
    print("LISTA DE DNI CORRECTOS ORDENADOS DE MENOR A MAYOR:", LISTA_DNI_CORRECTOS_MENOS_A_MAS)

elif opcion == 2:
    LISTA_DNI_INCORRECTOS_MENOS_A_MAS = sorted(LISTA_DNI_INCORRECTOS)
    print("LISTA DE DNI INCORRECTOS ORDENADOS DE MENOR A MAYOR:", LISTA_DNI_INCORRECTOS_MENOS_A_MAS)

elif opcion == 3:
    LISTA_TOTAL_DE_ERRORES = LISTA_INTENTOS.count(1) + LISTA_INTENTOS.count(2)
    print("Número total de errores:", LISTA_TOTAL_DE_ERRORES)

elif opcion == 4:
    print("Número total de DNIs correctos:", NUMERO_TOTAL_DNI_CORRECTO)

elif opcion == 5:
    PORCIENTO_DNI_CORRECTOS = (NUMERO_TOTAL_DNI_CORRECTO / len(LISTA_INTENTOS)) * 100
    PORCIENTO_DNI_INCORRECTOS = (LISTA_INTENTOS.count(2) / len(LISTA_INTENTOS)) * 100
    PORCIENTO_ERROR_LONGITUD = (LISTA_INTENTOS.count(1) / len(LISTA_INTENTOS)) * 100
    PORCIENTO_ERROR_NUMEROS = (LISTA_INTENTOS.count(0) / len(LISTA_INTENTOS)) * 100
    PORCIENTO_NO_EXISTENTES = 100 - (PORCIENTO_DNI_CORRECTOS + PORCIENTO_DNI_INCORRECTOS +
                                     PORCIENTO_ERROR_LONGITUD + PORCIENTO_ERROR_NUMEROS)

    print("PORCENTAJE de DNI correctos:", PORCIENTO_DNI_CORRECTOS)
    print("PORCENTAJE de DNI incorrectos:", PORCIENTO_DNI_INCORRECTOS)
    print("PORCENTAJE de Errores de longitud:", PORCIENTO_ERROR_LONGITUD)
    print("PORCENTAJE de Errores de números:", PORCIENTO_ERROR_NUMEROS)
    print("PORCENTAJE de No existentes:", PORCIENTO_NO_EXISTENTES)

elif opcion == 6:
    (calcular_letra_dni)