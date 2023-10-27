v1 = float(input("Introduce tu peso en Kg: "))
va1 = ("Kg")
v2 = float(input("Introduce tu estatura en m: "))
va2 = ("m")

total2 = (v2 * v2)
total1 = (v1 / total2)

print(("Si pesas"),v1,va1,("y tu altura es de "),v2,va2,("tu imc es:",total1))


if(total1 > 25 ): print("tienes sobrepeso")

else:print("Estas sano")
input()