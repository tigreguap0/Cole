#include <Servo.h>

int greenLedPin = 10; // Pin digital al que está conectado el LED verde
int yellowLedPin = 11; // Pin digital al que está conectado el LED amarillo
int redLedPin = 12; // Pin digital al que está conectado el LED rojo
int buzzerPin = 9; // Pin digital al que está conectado el buzzer
Servo barrierServo; // Crear un objeto Servo para controlar la barrera

const int greenTime = 5000; // Tiempo en milisegundos para el LED verde
const int yellowTime = 2000; // Tiempo en milisegundos para el LED amarillo
const int redTime = 5000; // Tiempo en milisegundos para el LED rojo

void setup() {
  pinMode(greenLedPin, OUTPUT); // Configura el pin del LED verde como salida
  pinMode(yellowLedPin, OUTPUT); // Configura el pin del LED amarillo como salida
  pinMode(redLedPin, OUTPUT); // Configura el pin del LED rojo como salida
  pinMode(buzzerPin, OUTPUT); // Configura el pin del buzzer como salida
  barrierServo.attach(8); // Conectar el servo motor al pin digital 8
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  // Semáforo en verde: barrera abierta
  digitalWrite(greenLedPin, HIGH);
  digitalWrite(yellowLedPin, LOW);
  digitalWrite(redLedPin, LOW);
  barrierServo.write(90); // Abre la barrera (90 grados)
  Serial.println("Green light - Barrier open");
  delay(greenTime); // Espera tiempo fijo con el LED verde encendido
  
  // Semáforo en amarillo: sonido de advertencia
  digitalWrite(greenLedPin, LOW);
  digitalWrite(yellowLedPin, HIGH);
  digitalWrite(redLedPin, LOW);
  Serial.println("Yellow light - Warning sound");
  for (int i = 0; i < (yellowTime / 500); i++) {
    digitalWrite(buzzerPin, HIGH); // Enciende el buzzer
    delay(250); // Suena durante 250 ms
    digitalWrite(buzzerPin, LOW); // Apaga el buzzer
    delay(250); // Silencio durante 250 ms
  }
  
  // Semáforo en rojo: barrera cerrada
  digitalWrite(greenLedPin, LOW);
  digitalWrite(yellowLedPin, LOW);
  digitalWrite(redLedPin, HIGH);
  barrierServo.write(0); // Cierra la barrera (0 grados)
  Serial.println("Red light - Barrier closed");
  delay(redTime); // Espera tiempo fijo con el LED rojo encendido
}
