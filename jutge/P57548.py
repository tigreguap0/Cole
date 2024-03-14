# Leer la primera entrada
a = int(input())

try:
    b = int(input())
except ValueError:
    b = a
    a = int(input())

suma = a + b

print(suma)