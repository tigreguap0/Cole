#include <Servo.h>

int ldrPin = A0; // Pin analógico al que está conectado la fotorresistencia (LDR)
Servo servoMotor; // Crear un objeto Servo para controlar el motor

void setup() {
  servoMotor.attach(9); // Conectar el servo motor al pin digital 9
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int ldrValue = analogRead(ldrPin); // Lee el valor analógico de la fotorresistencia
  
  Serial.print("LDR Value: ");
  Serial.println(ldrValue);
  
  if (ldrValue < 150) {
    servoMotor.write(45); // Mueve el servo a 45 grados si el valor es menor que 150
  } else if (ldrValue >= 150 && ldrValue <= 200) {
    servoMotor.write(90); // Mueve el servo a 90 grados si el valor está entre 150 y 200
  } else if (ldrValue > 200) {
    servoMotor.write(180); // Mueve el servo a 180 grados si el valor es mayor que 200
  }
  
  delay(1000); // Espera 1 segundo antes de realizar la siguiente lectura
}
