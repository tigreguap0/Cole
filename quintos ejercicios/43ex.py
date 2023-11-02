import time

palabra = input("Introduce una palabra: ")

for i, letra in enumerate(palabra):
    time.sleep(0.5)
    print(f"En la posición {i} está la {letra}")
