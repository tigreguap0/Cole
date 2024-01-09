lista = []
contador = 0
repeticiones = int(input("¿Cuantas veces deseas repeteir el programa? : "))
while(contador != repeticiones):
    numero = int(input("Introduce un numero: "))
    lista.append(numero)
    contador = contador + 1
print(lista)