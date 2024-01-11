lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

while True:
    valor_a_eliminar = input("Introduce el valor que deseas eliminar: ")

    if valor_a_eliminar.isdigit():
        valor_a_eliminar = int(valor_a_eliminar)

        if valor_a_eliminar in map(int, lista1):
            lista1 = [elemento for elemento in lista1 if (not elemento.isdigit()) or int(elemento) != valor_a_eliminar]
            print(lista1)
        else:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce valor numérico")

    continuar = input("Deseas introducir otro valor (s/n): ").lower()
    if continuar != 's':
        break
