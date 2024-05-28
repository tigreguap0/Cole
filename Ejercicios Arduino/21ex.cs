#include <Servo.h>

int buttonPin = 2; // Pin digital al que está conectado el botón
Servo servoMotor; // Crear un objeto Servo para controlar el motor
bool isDoorOpen = false; // Estado inicial de la puerta (cerrada)
bool lastButtonState = HIGH; // Estado anterior del botón (no pulsado)

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Configura el pin del botón como entrada con pull-up interno
  servoMotor.attach(9); // Conectar el servo motor al pin digital 9
  servoMotor.write(0); // Inicializa el servo en la posición cerrada (0 grados)
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  bool currentButtonState = digitalRead(buttonPin); // Lee el estado actual del botón

  // Detecta el cambio de estado del botón (flanco descendente)
  if (currentButtonState == LOW && lastButtonState == HIGH) {
    isDoorOpen = !isDoorOpen; // Alterna el estado de la puerta

    if (isDoorOpen) {
      servoMotor.write(90); // Mueve el servo a 90 grados para abrir la puerta
      Serial.println("Door opening...");
    } else {
      servoMotor.write(0); // Mueve el servo a 0 grados para cerrar la puerta
      Serial.println("Door closing...");
    }
  }

  lastButtonState = currentButtonState; // Actualiza el estado anterior del botón
  delay(100); // Pequeño retardo para debouncing
}
