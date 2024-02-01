import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class Jugador:
    def __init__(self):
        self.saldo = 1000

# Función para mover las letras
def mover_letra(canvas, letra, distancia):
    canvas.move(letra, distancia, 0)

# Función para simular la carrera
def simular_carrera(jugador):
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Carrera de Caballos (con letras)")

    # Configurar el lienzo
    canvas = tk.Canvas(ventana, width=800, height=600)
    canvas.pack()

    # Crear las letras (caballos)
    letras = []
    for i in range(4):
        letra = canvas.create_text(50, 50 + i * 100, text=chr(65 + i), font=("Arial", 24))
        letras.append(letra)

    # Pedir al usuario que introduzca la cantidad a apostar
    cantidad_apostada = simpledialog.askinteger("Apuesta", "Introduce la cantidad a apostar:", minvalue=100, maxvalue=jugador.saldo)
    caballo_apostado = simpledialog.askstring("Apuesta", "A qué caballo le apuestas? (A/B/C/D):")

    # Correr la carrera
    ganador = None
    while True:
        # Mover cada letra una distancia aleatoria
        for letra in letras:
            mover_letra(canvas, letra, random.randint(1, 20))

            # Si una letra llega al final, detener la carrera
            if canvas.coords(letra)[0] > 750:
                ganador = chr(65 + letras.index(letra))
                break

        if ganador:
            break

        # Actualizar la ventana
        ventana.update()
        ventana.after(100)

    # Mostrar el mensaje del ganador
    if ganador:
        messagebox.showinfo("Fin de la Carrera", f"La letra {ganador} ha ganado la carrera!")

        # Actualizar el saldo según el resultado de la carrera
        if caballo_apostado.upper() == ganador:
            jugador.saldo += cantidad_apostada * 4
        else:
            jugador.saldo -= cantidad_apostada

        messagebox.showinfo("Saldo Actual", f"Tu saldo actual es de {jugador.saldo}")
    else:
        messagebox.showinfo("Fin de la Carrera", "La carrera ha terminado sin un ganador.")

    # Preguntar al usuario si desea apostar nuevamente
    respuesta = messagebox.askyesno("¿Desea apostar nuevamente?", "¿Desea iniciar una nueva carrera?")
    if respuesta and jugador.saldo >= 100:
        simular_carrera(jugador)
    else:
        ventana.destroy()

class JuegoRuleta:
    def __init__(self, root, jugador):
        self.root = root
        self.root.title("Juego de Ruleta")
        self.jugador = jugador
        
        # Cargar la imagen de la ruleta
        ruta_imagen_ruleta = r'C:\\Users\\FalomirSerbanMiguel\\Documents\\GitHub\\Cole\\Proyecto Menu Juegos\\roulette.png'
        self.imagen_ruleta = tk.PhotoImage(file=ruta_imagen_ruleta)
        self.label_imagen = tk.Label(root, image=self.imagen_ruleta)
        self.label_imagen.pack()

        # Crear botón para girar la ruleta
        self.boton_girar = tk.Button(root, text="Girar Ruleta", height=2, width=15, command=self.girar_ruleta)
        self.boton_girar.place(x=444, y=300)
    
        self.boton_saldo = tk.Button(root, text="Mostrar saldo", height=2, width=10, command=self.mostrar_dinero)
        self.boton_saldo.place(x=100, y=420)

    def mostrar_dinero(self):
        messagebox.showinfo("Resultado y Saldo", f"{self.jugador.saldo}")

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
        self.jugador.saldo += ganancia_perdida

        # Mostrar el resultado y saldo actual
        mensaje_resultado = f"Resultado de la apuesta: {ganancia_perdida}€"
        mensaje_saldo = f"Tu saldo actual es de {self.jugador.saldo}€."
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
    def __init__(self, jugador):
        super().__init__()
        self.title("Blackjack")
        self.geometry("200x100")
        self.jugador = jugador

        self.nombre_label = tk.Label(self, text="Ingresa tu nombre:")
        self.nombre_label.pack()
        
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()
        
        self.iniciar_button = tk.Button(self, text="Iniciar Juego", command=self.iniciar_juego)
        self.iniciar_button.pack()

    def iniciar_juego(self):
        nombre_jugador = self.nombre_entry.get()
        dinero_actual = self.jugador.saldo

        while dinero_actual > 0:
            messagebox.showinfo("Dinero actual", f"Dinero actual: {dinero_actual}")

            listacartas = list(valores_cartas.keys()) * 4
            random.shuffle(listacartas)

            mano_jugador = [listacartas.pop(), listacartas.pop()]
            mano_banca = [listacartas.pop(), listacartas.pop()]

            while True:
                messagebox.showinfo("Mano del jugador", f"Mano del jugador: {mano_jugador}, Valor: {self.asignar_valor(mano_jugador)}")
                messagebox.showinfo("Primera carta de la banca", f"Primera carta de la banca: {mano_banca[0]}")

                if self.asignar_valor(mano_jugador) == 21:
                    messagebox.showinfo("¡Blackjack!", "¡Ganaste!")
                    dinero_actual += self.jugador.saldo
                    break

                accion = messagebox.askquestion("¿Quieres pedir otra carta?", "¿Quieres pedir otra carta?")

                if accion == 'yes':
                    nueva_carta = listacartas.pop()
                    mano_jugador.append(nueva_carta)
                    messagebox.showinfo("Nueva carta", f"Has recibido una carta: {nueva_carta}")
                    
                    if self.asignar_valor(mano_jugador) > 21:
                        messagebox.showinfo("¡Te pasaste!", "Has sobrepasado 21. ¡Perdiste!")
                        dinero_actual -= self.jugador.saldo
                        break
                else:
                    while self.asignar_valor(mano_banca) < 17:
                        nueva_carta_banca = listacartas.pop()
                        mano_banca.append(nueva_carta_banca)

                    messagebox.showinfo("Mano de la banca", f"Mano de la banca: {mano_banca}, Valor: {self.asignar_valor(mano_banca)}")

                    if self.asignar_valor(mano_banca) > 21:
                        messagebox.showinfo("¡La banca se pasó!", "¡Ganaste!")
                        dinero_actual += self.jugador.saldo
                        break

                    if self.asignar_valor(mano_jugador) > self.asignar_valor(mano_banca):
                        messagebox.showinfo("¡Ganaste!", "Tu valor es mayor que el de la banca. ¡Ganaste!")
                        dinero_actual += self.jugador.saldo
                        break
                    else:
                        messagebox.showinfo("¡Perdiste!", "El valor de la banca es mayor que el tuyo. ¡Perdiste!")
                        dinero_actual -= self.jugador.saldo
                        break

            continuar = messagebox.askquestion("¿Quieres jugar otra ronda?", "¿Quieres jugar otra ronda?")

            if continuar == 'no':
                break
        
        messagebox.showinfo("¡Gracias por jugar!", f"Tu dinero final es: {dinero_actual}")

    def asignar_valor(self, mano):
        valor_mano = 0
        ases = 0

        for carta in mano:
            if "As" in carta:
                ases += 1
            valor_carta = valores_cartas[carta]
            if isinstance(valor_carta, tuple):
                valor_mano += max(valor_carta)
            else:
                valor_mano += valor_carta

        while valor_mano > 21 and ases:
            valor_mano -= 10
            ases -= 1

        return valor_mano

jugador = Jugador()

# Crear la ventana principal del menú
ventana_menu = tk.Tk()
ventana_menu.title("Menú de Juegos")

# Funciones para abrir cada juego
def abrir_carrera_caballos():
    simular_carrera(jugador)

def abrir_ruleta():
    juego_ruleta = JuegoRuleta(ventana_menu, jugador)

def abrir_blackjack():
    juego_blackjack = BlackjackGUI(jugador)

# Botones para abrir cada juego
boton_carrera_caballos = tk.Button(ventana_menu, text="Carrera de Caballos", command=abrir_carrera_caballos)
boton_carrera_caballos.pack(pady=10)

boton_ruleta = tk.Button(ventana_menu, text="Ruleta", command=abrir_ruleta)
boton_ruleta.pack(pady=10)

boton_blackjack = tk.Button(ventana_menu, text="Blackjack", command=abrir_blackjack)
boton_blackjack.pack(pady=10)

# Ejecutar el bucle principal del menú
ventana_menu.mainloop()
