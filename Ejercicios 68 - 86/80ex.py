def es_decimal(numero):
    try:
        float(numero)
        if "." in numero:
            return "Es un número con decimales"
        else:
            return "No es un número con decimales"
    except ValueError:
        return "No es un número con decimales"

numeros = ["12", "12.1", "Hola", "12.", "6.098", "6.09a", "4.34.2"]

for numero in numeros:
    print(es_decimal(numero))
