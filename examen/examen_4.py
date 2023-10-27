import time

print("****GASOLINERA****")
time.sleep(0.5)
print("1. Sin plomo 95")
time.sleep(0.5)
print("2. Sin plomo 98")
time.sleep(0.5)
print("3. Gasóleo A")
time.sleep(0.5)
print("4. Gasóleo A+")
time.sleep(0.5)
print("****GASOLINERA****")

x = input("Introduce un numero del 1 al cuatro respecto al menu: ")

time.sleep(0.5)

litros = float(input("Introduce la cantidad de litros que quieres repostar: "))

if x == ("1"):
    plomo95 = (litros * 1.765)
    print("El combustible a pagar es de: ",plomo95)

if x == ("2"):
    plomo98 = (litros * 1.913)
    print("Enorabuena tiene un 10 % ")
    plomo98_descuento = (plomo98 * 0.10)
    resultado1 = (plomo98 - plomo98_descuento)
    print("El combustible a pagar es de: ",resultado1)

if x == ("3"):
    GasoleoA = (litros * 1.746)
    print("El combustible a pagar es de: ",GasoleoA)

if x == ("4"):
    Gasoleo_a_mas = (litros * 1.839)
    print("Enorabuena tienes un 12%")
    Gasoleo_A_mas_descuento = (Gasoleo_a_mas * 0.12)
    resultado_4 = (Gasoleo_a_mas - Gasoleo_A_mas_descuento) 
    print("El combustible a pagar es de: ",resultado_4)

