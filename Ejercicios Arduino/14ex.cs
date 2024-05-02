// Definir los pines
const int buzzerPin = 13;
const int buttonPin = 9;
const int ledPin = 1;
const int ledPin1 = 5;
// Variables para controlar el juego
unsigned long soundDuration;  // Duración del sonido
unsigned long startTime;      // Cuando comienza a presionar el botón
unsigned long buttonPressDuration;  // Duración de la presión del botón

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin1, OUTPUT);
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  soundDuration = random(1000, 10001);  // Genera un tiempo aleatorio entre 1 y 10 segundos
  tone(buzzerPin, 1000, soundDuration); // Emite un tono en el buzzer
  delay(soundDuration + 100);  // Espera hasta que el sonido termine más un pequeño margen

  // Espera a que el usuario presione el botón
  while(digitalRead(buttonPin) == LOW);

  startTime = millis(); // Registra cuando el usuario comenzó a presionar el botón

  // Espera a que el usuario suelte el botón
  while(digitalRead(buttonPin) == HIGH);
  buttonPressDuration = millis() - startTime;  // Calcula cuánto tiempo se presionó el botón

  // Chequea si el usuario ganó o perdió
  if (abs((long)buttonPressDuration - (long)soundDuration) <= 500) {  // 500 ms de margen de error
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    Serial.println("¡Ganaste!");
  } else {
    digitalWrite(ledPin1, HIGH);
    delay(500);
    digitalWrite(ledPin1, LOW);
    Serial.println("Perdiste. Intenta nuevamente.");
  }

  delay(2000);  // Espera antes de comenzar un nuevo juego
}
