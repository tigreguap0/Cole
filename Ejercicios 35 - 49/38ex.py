try:
    num_notas = int(input("Introduce el número de notas que deseas introducir: "))
except ValueError:
    print("Error: Debes ingresar un número entero para el número de notas.")
    exit()

notas_aprobadas = 0

for i in range(num_notas):
    try:
        nota = float(input(f"Introduce la nota {i + 1}: "))
        if nota >= 5.0:
            print("Aprobado")
            notas_aprobadas += 1
        else:
            print("Suspendido")
    except ValueError:
        print("Error: Debes ingresar un número para la nota.")

print(f"Total de notas aprobadas: {notas_aprobadas}/{num_notas}")
