
var_numero = input("Introduce una cifra de 4 números: ")


var_longitud = len(var_numero)
print("Longitud:", var_longitud)


if var_longitud != 4:
    print("La cifra no tiene 4 dígitos.")
else:
    
    digito1 = int(var_numero[0])
    digito2 = int(var_numero[1])
    digito3 = int(var_numero[2])
    digito4 = int(var_numero[3])

    var_suma = digito1 + digito2 + digito3 + digito4
    print("Suma de los dígitos:", var_suma)

    
    if var_suma % 2 == 0:
        print(f"El valor de {var_suma} es par.")
    else:
        print(f"El valor de {var_suma} es impar.")
