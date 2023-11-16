repetir = "s"
repeticiones = 0
resultados = 0
while repetir == "s":
    v1 = int(input("Dime tu primer numero: "))
    v2 = int(input("Dime tu segundo numero: "))
    resultado = (v1 + v2)
    repeticiones = repeticiones + 1
    resultados = (resultados + resultado)
    print(resultado)
    repetir = input("deseas repetir (s / n): ")
print("La suma total es: ",resultados, "y llevas estas repeticiones: ",repeticiones)