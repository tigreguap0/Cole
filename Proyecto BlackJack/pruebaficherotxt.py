def guardar_resultados(nombre, dinero_apostado, dinero_ganado):
    try:
        with open(r"C:\Users\FalomirSerbanMiguel\Documents\GitHub\Cole\Proyecto BlackJack\top.txt", "a") as f:
            f.write(f"Nombre: {nombre}, Dinero Apostado: {dinero_apostado}, Dinero Ganado: {dinero_ganado}\n")
    except Exception as error:
        print(f"Error al intentar escribir en el archivo: {error}")


with open("top.txt", "a") as f:



with open("top.txt", "a") as f:
    f.write(f"Nombre: {nombre}, Dinero Apostado: {dinero_apostado}, Dinero Ganado: {dinero_ganado}\n")
    print("Información escrita en el archivo.")



def guardar_resultados(nombre, dinero_ingresado, dinero_apostado, dinero_ganado):
    with open(r"C:\Users\FalomirSerbanMiguel\Documents\GitHub\Cole\Proyecto BlackJack\top.txt", "a") as f:
        f.write(f"Nombre: {nombre}, Dinero Ingresado: {dinero_ingresado}, Dinero Apostado: {dinero_apostado}, Dinero Ganado: {dinero_ganado}\n")


