try:
    num_veces = int(input("Introduce el número de notas que deseas introducir: "))
except ValueError:
    print("Error: Debes ingresar un número entero para el número de notas.")
    exit()

for i in range(num_veces):
    try:
        numero = float(input(f"Introduce tu primero numero {i + 1}: "))
        if numero < 0:
            print("negativo")
        else:
            print("positivo")
    except ValueError:
        print("Error: Debes ingresar un número")

