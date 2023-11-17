import random
import time

tiempo_deseado = 3.0

resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

tiempo_inicio = time.time()

while time.time() - tiempo_inicio < tiempo_deseado:
    resultado = random.randint(1, 6)
    resultados[resultado] += 1

print("RESUMEN")
print("Tiempo:", time.time() - tiempo_inicio)
for num, count in resultados.items():
    print(f"{num}: {count}")
