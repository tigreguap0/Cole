def mostrar_valores():
    # Solicitar al usuario los números y el intervalo
    inicio = int(input("Introduce el número de inicio: "))
    fin = int(input("Introduce el número de fin: "))
    intervalo = int(input("Introduce el intervalo: "))

    # Validar que el intervalo sea mayor que 0
    if intervalo <= 0:
        print("Por favor, introduce un intervalo mayor que 0.")
        return

    # Mostrar los valores en el rango con el intervalo especificado
    valores = []
    while inicio <= fin:
        valores.append(str(inicio))
        inicio += intervalo

    # Imprimir los valores en el formato deseado
    resultado = ",".join(valores)
    print(resultado)

# Llamar a la función
mostrar_valores()
