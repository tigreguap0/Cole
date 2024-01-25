import os
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# Ruta de la imagen de la ruleta
ruta_imagen_ruleta = r'C:\\Users\\FalomirSerbanMiguel\\Documents\\GitHub\\Cole\\Proyecto La arruina vidas\\roulette.png'

class JuegoRuleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Ruleta")
        
        # Cargar la imagen de la ruleta
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

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoRuleta(root)
    root.mainloop()
