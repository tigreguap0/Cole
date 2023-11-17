import random

frecuencia_dados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(100):
    resultado_dado = random.randint(1, 6)
    
    frecuencia_dados[resultado_dado] += 1

# Imprimir los resultados
for numero, frecuencia in frecuencia_dados.items():
    print(f"{numero}: {frecuencia}")
