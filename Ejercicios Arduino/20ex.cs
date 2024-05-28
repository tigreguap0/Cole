#include <Servo.h>

int openButtonPin = 2; // Pin digital al que está conectado el botón de abrir
int closeButtonPin = 3; // Pin digital al que está conectado el botón de cerrar
Servo servoMotor; // Crear un objeto Servo para controlar el motor

void setup() {
  pinMode(openButtonPin, INPUT_PULLUP); // Configura el pin del botón de abrir como entrada con pull-up interno
  pinMode(closeButtonPin, INPUT_PULLUP); // Configura el pin del botón de cerrar como entrada con pull-up interno
  servoMotor.attach(9); // Conectar el servo motor al pin digital 9
  servoMotor.write(0); // Inicializa el servo en la posición cerrada (0 grados)
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int openButtonState = digitalRead(openButtonPin); // Lee el estado del botón de abrir
  int closeButtonState = digitalRead(closeButtonPin); // Lee el estado del botón de cerrar

  if (openButtonState == LOW) { // Si el botón de abrir está pulsado
    servoMotor.write(90); // Mueve el servo a 90 grados para abrir la puerta
    Serial.println("Door opening...");
  }

  if (closeButtonState == LOW) { // Si el botón de cerrar está pulsado
    servoMotor.write(0); // Mueve el servo a 0 grados para cerrar la puerta
    Serial.println("Door closing...");
  }

  delay(100); // Pequeño retardo para debouncing
}
