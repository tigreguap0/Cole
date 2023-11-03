import math
import time

print("Ejemplo: 3x^2 + 2x + 5 = y")
a = float(input("Introduce el primer valor: "))
b = float(input("Introduce el segundo valor: "))
x = float(input("Introduce el tercer valor: "))

if x < 0:
    print("Error: El valor de x no puede ser negativo.")
else:
    print(f"{a}x^2 + {b}x + {x} = y")
    print("Calculando...")
    time.sleep(1)
    print("Calculando..")
    time.sleep(1)
    print("Calculando.")
    time.sleep(1)
    print("Calculando..")
    time.sleep(1)
    print("Calculando...")
    time.sleep(1)

    discriminante = b**2 - 4*a*x

    if discriminante < 0:
        print("No hay soluciones reales para esta ecuación.")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("El resultado para x1 es:", x1)
        print("El resultado para x2 es:", x2)


