# Leer la entrada
entrada = input().split()

# Si hay dos números en la entrada en una sola línea
if len(entrada) == 2:
    # Convertir los números a enteros
    num1 = int(entrada[0])
    num2 = int(entrada[1])
# Si hay dos números en dos líneas separadas
else:
    # Leer los dos números por separado
    num1 = int(entrada[0])
    num2 = int(input())

# Calcular la suma
suma = num1 + num2

# Imprimir la suma
print(suma)