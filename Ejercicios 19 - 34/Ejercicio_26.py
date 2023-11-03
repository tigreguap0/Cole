var1=input("Introduce una palabra y detectare si la primera es mayuscula lo detectare y lo mismo si esta en minuscula: oH")

if var1.islower()==True:
    print("es minúscula")

if var1.isupper()==True:
    print("es mayúscula")

elif var1.isnumeric()==True:
    print("Es un numero")


