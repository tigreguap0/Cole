ingles = []
castellano = []
catalan = []

repetir = "s"

while repetir != "n":
    nombre = input("Introduce estudiante: ")
    
    nota_ingles = float(input("Nota inglés: "))
    nota_castellano = float(input("Nota castellano: "))
    nota_catalan = float(input("Nota catalán: "))
    
    ingles.append(nota_ingles)
    castellano.append(nota_castellano)
    catalan.append(nota_catalan)
    
    repetir = input("Deseas introducir otro alumno s/n: ")

print("Inglés:", ingles)
print("Castellano:", castellano)
print("Catalán:", catalan)

media_ingles = sum(ingles) / len(ingles)
media_castellano = sum(castellano) / len(castellano)
media_catalan = sum(catalan) / len(catalan)

mediana_ingles = sorted(ingles)[len(ingles) // 2]
mediana_castellano = sorted(castellano)[len(castellano) // 2]
mediana_catalan = sorted(catalan)[len(catalan) // 2]

print("La media en inglés es:", media_ingles)
print("La media en castellano es:", media_castellano)
print("La media en catalán es:", media_catalan)

print("La mediana en inglés es:", mediana_ingles)
print("La mediana en castellano es:", mediana_castellano)
print("La mediana en catalán es:", mediana_catalan)
