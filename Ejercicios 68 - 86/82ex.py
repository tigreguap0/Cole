import random
lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']
print("Estas son las palabras que puede haber: ",lista)
valor_al_azar = random.choice(lista)
contador = 0
while contador !=1:
    comprobacion = input("Introduce la palabra secreta: ")
    if comprobacion == valor_al_azar:
        print("Acertaste")
        contador = contador + 1
    else:
        print("Sigue jugando")

