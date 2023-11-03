# Definición de variables y asignación de valores
Var1 = float(input("Introduce el primer numero: "))
Var2 = float(input("Introduce el segundo número: "))

# Compara el contenido de ambas variables para saber qué número es mayor
if Var1 > Var2:
    # Si la condición se cumple, se visualiza el siguiente mensaje
    print("El número", Var1, "es mayor que", Var2)
elif Var1 < Var2:
    # Si la condición se cumple, se visualiza el siguiente mensaje
    print("El número", Var2, "es mayor que", Var1)
else:
    # Si ninguna de las condiciones anteriores se cumple, se visualiza el siguiente mensaje
    print("Ambos numeros son iguales")
