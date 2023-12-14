total = 50
valor = 1
while(valor != 0):
    valor = int(input("Introduce un valor: "))
    if valor % 2:
        total = total - valor
        print(total)
    else:
        total = total + valor
        print(total)