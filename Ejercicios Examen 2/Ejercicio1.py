i=1
positivos = 0
negativos = 0
while(i!=6):
    n1 = int(input("Introduce un numero: "))
    if n1 > 0:
        positivos = positivos + 1
        i = i+1
    else:
        negativos = negativos + 1
        i = i+1

print("Numero positivos: ",positivos)
print("Numero negativos: ",negativos)