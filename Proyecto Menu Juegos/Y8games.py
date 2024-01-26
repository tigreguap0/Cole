import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class JuegoRuleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Ruleta")
        
        # Cargar la imagen de la ruleta
        ruta_imagen_ruleta = r'C:\\Users\\FalomirSerbanMiguel\\Documents\\GitHub\\Cole\\Proyecto Menu Juegos\\roulette.png'
        self.imagen_ruleta = tk.PhotoImage(file=ruta_imagen_ruleta)
        self.label_imagen = tk.Label(root, image=self.imagen_ruleta)
        self.label_imagen.pack()

        # Crear botón para girar la ruleta
        self.boton_girar = tk.Button(root, text="Girar Ruleta", height=2, width=15, command=self.girar_ruleta)
        self.boton_girar.place(x=444, y=300)
    
        self.boton_saldo = tk.Button(root, text="Mostrar saldo", height=2, width=10, command=self.mostrar_dinero)
        self.boton_saldo.place(x=815, y=325)

        # Inicializar el saldo del jugador
        self.saldo = 1000

    def mostrar_dinero(self):
        messagebox.showinfo("Resultado y Saldo", f"{self.saldo}")

    def girar_ruleta(self):
        # Simular el giro de la ruleta
        resultado_ruleta = random.randint(0, 36)

        # Mostrar el resultado en un cuadro de mensaje
        mensaje = f"La ruleta ha girado y el resultado es: {resultado_ruleta}"
        messagebox.showinfo("Resultado", mensaje)

        # Evaluar la apuesta y actualizar el saldo del jugador
        tipo_apuesta = simpledialog.askstring("Tipo de Apuesta", "Ingresa el tipo de apuesta (numero/rango1/rango2/rango3/par/impar/rojo/negro):", parent=self.root)
        monto_apostado = simpledialog.askinteger("Monto de Apuesta", "Ingresa el monto a apostar:", parent=self.root)

        ganancia_perdida = self.evaluar_apuesta(tipo_apuesta, None, monto_apostado, resultado_ruleta)  # Puedes ingresar el número apostado en lugar de None
        self.saldo += ganancia_perdida

        # Mostrar el resultado y saldo actual
        mensaje_resultado = f"Resultado de la apuesta: {ganancia_perdida}€"
        mensaje_saldo = f"Tu saldo actual es de {self.saldo}€."
        messagebox.showinfo("Resultado y Saldo", f"{mensaje_resultado}\n{mensaje_saldo}")

    def evaluar_apuesta(self, tipo_apuesta, numero_apuesta, monto_apostado, resultado_ruleta):
        """Evalúa si la apuesta es ganadora o perdedora y actualiza el saldo del jugador."""
        if tipo_apuesta == "numero":
            return monto_apostado if numero_apuesta == resultado_ruleta else -monto_apostado
        elif tipo_apuesta == "rango1" and 1 <= resultado_ruleta <= 12:
            return monto_apostado
        elif tipo_apuesta == "rango2" and 2 <= resultado_ruleta <= 13:
            return monto_apostado
        elif tipo_apuesta == "rango3" and (22 <= resultado_ruleta <= 22 or 25 <= resultado_ruleta <= 33):
            return monto_apostado
        elif tipo_apuesta == "par" and resultado_ruleta % 2 == 0:
            return monto_apostado
        elif tipo_apuesta == "impar" and resultado_ruleta % 2 != 0:
            return monto_apostado
        elif tipo_apuesta == "rojo" and resultado_ruleta in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            return monto_apostado
        elif tipo_apuesta == "negro" and resultado_ruleta in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            return monto_apostado
        else:
            return -monto_apostado

valores_cartas = {
    "Rey♦ (10)": 10, "Reina♦ (10)": 10, "Jota♦ (10)": 10, "Diez♦ (10)": 10, "Nueve♦ (9)": 9, "Ocho♦ (8)": 8, "Siete♦ (7)": 7,
    "Seis♦ (6)": 6, "Cinco♦ (5)": 5, "Cuatro♦ (4)": 4, "Tres♦ (3)": 3, "Dos♦ (2)": 2, "As♦ (1, 11)": (1, 11),
    "Rey♥ (10)": 10, "Reina♥ (10)": 10, "Jota♥ (10)": 10, "Diez♥ (10)": 10, "Nueve♥ (9)": 9, "Ocho♥ (8)": 8, "Siete♥ (7)": 7,
    "Seis♥ (6)": 6, "Cinco♥ (5)": 5, "Cuatro♥ (4)": 4, "Tres♥ (3)": 3, "Dos♥ (2)": 2, "As♥ (1, 11)": (1, 11),
    "Rey♠ (10)": 10, "Reina♠ (10)": 10, "Jota♠ (10)": 10, "Diez♠ (10)": 10, "Nueve♠ (9)": 9, "Ocho♠ (8)": 8, "Siete♠ (7)": 7,
    "Seis♠ (6)": 6, "Cinco♠ (5)": 5, "Cuatro♠ (4)": 4, "Tres♠ (3)": 3, "Dos♠ (2)": 2, "As♠ (1, 11)": (1, 11),
    "Rey♣ (10)": 10, "Reina♣ (10)": 10, "Jota♣ (10)": 10, "Diez♣ (10)": 10, "Nueve♣ (9)": 9, "Ocho♣ (8)": 8, "Siete♣ (7)": 7,
    "Seis♣(6)": 6, "Cinco♣ (5)": 5, "Cuatro♣ (4)": 4, "Tres♣ (3)": 3, "Dos♣ (2)": 2, "As♣ (1, 11)": (1, 11),
}

listacartas = list(valores_cartas.keys()) * 4

class BlackjackGUI(tk.Tk):    
    def __init__(self):
        super().__init__()
        self.title("Blackjack")
        self.geometry("200x100")
        
        self.nombre_label = tk.Label(self, text="Ingresa tu nombre:")
        self.nombre_label.pack()
        
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()
        
        self.iniciar_button = tk.Button(self, text="Iniciar Juego", command=self.iniciar_juego)
        self.iniciar_button.pack()

    def iniciar_juego(self):
        nombre_jugador = self.nombre_entry.get()
        dinero_ingresado = self.obtener_cantidad_dinero()
        dinero_actual = dinero_ingresado

        while dinero_actual > 0:
            messagebox.showinfo("Dinero actual", f"Dinero actual: {dinero_actual}")
            apuesta_actual = self.obtener_apuesta_actual(dinero_actual)

            listacartas = list(valores_cartas.keys()) * 4
            random.shuffle(listacartas)

            mano_jugador = [listacartas.pop(), listacartas.pop()]
            mano_banca = [listacartas.pop(), listacartas.pop()]

            while True:
                messagebox.showinfo("Mano del jugador", f"Mano del jugador: {mano_jugador}, Valor: {self.asignar_valor(mano_jugador)}")
                messagebox.showinfo("Primera carta de la banca", f"Primera carta de la banca: {mano_banca[0]}")

                if self.asignar_valor(mano_jugador) == 21:
                    messagebox.showinfo("¡Blackjack!", "¡Ganaste!")
                    dinero_actual += apuesta_actual
                    break

                accion = messagebox.askquestion("¿Quieres pedir otra carta?", "¿Quieres pedir otra carta?")

                if accion == 'yes':
                    nueva_carta = listacartas.pop()
                    mano_jugador.append(nueva_carta)
                    messagebox.showinfo("Nueva carta", f"Has recibido una carta: {nueva_carta}")

                    if self.asignar_valor(mano_jugador) > 21:
                        messagebox.showinfo("Te has pasado de 21", "¡Has perdido!")
                        dinero_actual -= apuesta_actual
                        break
                else:
                    while self.asignar_valor(mano_banca) < 17:
                        carta_banca = listacartas.pop()
                        mano_banca.append(carta_banca)
                        messagebox.showinfo("La banca ha recibido una carta", f"La banca ha recibido una carta: {carta_banca}")

                    messagebox.showinfo("Mano del jugador", f"Mano del jugador: {mano_jugador}, Valor TOTAL: {self.asignar_valor(mano_jugador)}")
                    messagebox.showinfo("Mano de la banca", f"Mano de la banca: {mano_banca}, Valor TOTAL: {self.asignar_valor(mano_banca)}")

                    if self.asignar_valor(mano_banca) > 21:
                        messagebox.showinfo("La banca se ha pasado de 21", "¡Ganaste!")
                        dinero_actual += apuesta_actual
                        break
                    elif self.asignar_valor(mano_jugador) > self.asignar_valor(mano_banca):
                        messagebox.showinfo("¡Ganaste!", "¡Ganaste!")
                        dinero_actual += apuesta_actual
                        break
                    elif self.asignar_valor(mano_jugador) < self.asignar_valor(mano_banca):
                        messagebox.showinfo("¡Perdiste!", "¡Perdiste!")
                        dinero_actual -= apuesta_actual
                        break
                    else:
                        messagebox.showinfo("Empate", "Empate. Nadie gana.")
                        break

            messagebox.showinfo("Dinero ganado", f"Dinero ganado: {dinero_actual - dinero_ingresado}")

            self.guardar_resultados(nombre_jugador, dinero_ingresado, apuesta_actual, dinero_actual - dinero_ingresado)

            jugar_nuevamente = messagebox.askquestion("¿Quieres jugar otra vez?", "¿Quieres jugar otra vez?")
            if jugar_nuevamente != 'yes':
                break

        messagebox.showinfo("Gracias por jugar", "¡Hasta luego!")

    def asignar_valor(self, cartas):
        valor = sum(valores_cartas[carta] if type(valores_cartas[carta]) == int else max(valores_cartas[carta]) for carta in cartas)
        if "As" in cartas and valor + 10 <= 21:
            valor += 10
        return valor

    def guardar_resultados(self, nombre, dinero_ingresado, dinero_apostado, dinero_ganado):
        with open("top.txt", "a") as f:
            f.write(f"Nombre: {nombre}, Dinero Ingresado: {dinero_ingresado}, Dinero Apostado: {dinero_apostado}, Dinero Ganado: {dinero_ganado}\n")

    def obtener_cantidad_dinero(self):
        while True:
            try:
                dinero = float(simpledialog.askstring("Cantidad de dinero", "Ingresa la cantidad de dinero que deseas jugar: "))
                return dinero
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def obtener_apuesta_actual(self, dinero_actual):
        while True:
            try:
                apuesta = float(simpledialog.askstring("Apuesta", "¿Cuánto deseas apostar?: "))
                if apuesta <= dinero_actual:
                    return apuesta
                else:
                    messagebox.showerror("Error", "No puedes apostar más dinero del que tienes. Introduce una apuesta válida.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def mostrar_menu():
    juego = simpledialog.askstring("Menú de Juegos", "¿A qué quieres jugar?\n\nEscribe 'R' para Ruleta o 'BJ' para Blackjack:")
    return juego

def main():
    # Mostrar el menú y obtener la elección del usuario
    opcion = mostrar_menu()

    if opcion == "R":
        root = tk.Tk()
        juego = JuegoRuleta(root)
        root.mainloop()
    elif opcion == "BJ":
        app = BlackjackGUI()
        app.mainloop()
    else:
        messagebox.showerror("Error", "Opción inválida. Por favor, elige 'R' para Ruleta o 'BJ' para Blackjack.")

if __name__ == "__main__":
    main()
