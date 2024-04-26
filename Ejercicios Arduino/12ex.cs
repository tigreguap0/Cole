// Define los pines para los LEDs y el zumbador
int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int buzzerPin = 8;

// Variables para contar las apariciones de los LEDs
int greenCount = 0;
int redCount = 0;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Enciende el LED verde
  digitalWrite(greenPin, HIGH);
  delay(1000);
  digitalWrite(greenPin, LOW);
  greenCount++; // Incrementa el contador de verde
  delay(1000);
  
  // Enciende el LED azul
  digitalWrite(bluePin, HIGH);
  delay(1000);
  digitalWrite(bluePin, LOW);
  delay(1000);

  // Enciende el LED rojo
  digitalWrite(redPin, HIGH);
  delay(1000);
  digitalWrite(redPin, LOW);
  redCount++; // Incrementa el contador de rojo
  delay(1000);
  
  // Cada 5 veces que el LED rojo se enciende, suena un pitido
  if (redCount >= 5) {
    tone(buzzerPin, 1000, 500); // Emite un pitido a 1000 Hz durante 500 ms
    redCount = 0; // Resetea el contador de rojo
  }
}
