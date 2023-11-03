import math
import time
num1 = float(input("Escoge un numero: "))
num2 = float(input("Escoge un numero: "))

print("Menu...")
time.sleep(1)
print("Loading")
time.sleep(1)
print("Loading.")
time.sleep(1)
print("Loading..")
time.sleep(1)
print("Loading...")
time.sleep(1)
print("Escoge + para sumar")
print("Escoge - para restar")
print("Escoge * para multiplicar")
print("Escoge ** para elevarlo al cuadrado")
print("Escoge // para realizar la operacion")
print("Escoge % para hacer un porcentage")
print("Escoge & para hacer la raiz cuadrada(solamente funciona con el primer numero)")


operacion = input("")

if operacion == ("+"):
    print("De acuerdo vamos a hacer la suma: ")
    resultado_suma = (num1 + num2)
    print("El resultado es: ",resultado_suma)

if operacion == ("-"):
    print("De acuerdo vamos a hacer la resta: ")
    resultado_resta = (num1 - num2)
    print("El resultado es: ",resultado_resta)

if operacion == ("*"):
    print("De acuerdo vamos a hacer la multiplicacion: ")
    resultado_multiplicacion = (num1 * num2)
    print("El resultado es: ",resultado_multiplicacion)

if operacion == ("**"):
    print("De acuerdo vamos a elevarlo al cuadrado: ")
    resultado_cuadrado = (num1 ** num2)
    print("El resultado es: ",resultado_cuadrado)

if operacion == ("//"):
    print("De acuerdo vamos a hacer la operacion: ")
    resultado_barrabarra = (num1 // num2)
    print("El resultado es: ",resultado_barrabarra)

if operacion == ("/"):
    print("De acuerdo vamos a hacer la division: ")
    resultado_division = (num1 + num2)
    print("El resultado es: ",resultado_division)

if operacion == ("%"):
    print("De acuerdo vamos a hacer el porcentage: ")
    resultado_porcentage = (num1 % num2)
    print("El resultado es: ",resultado_porcentage)

if operacion == ("&"):
    print("De acuerdo vamos a hacer la raiz solamente del numero 1: ")
    resultado_raiz = (math.sqrt(num1))
    print("El resultado es: ",resultado_raiz)

