// Define los pines donde se conectan los LEDs
int ledPin1 = 9;
int ledPin2 = 10;

// La función setup() se ejecuta una vez cuando se reinicia o se enciende la placa
void setup() {
  // Configura los pines del LED como salida
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

// La función loop() se ejecuta continuamente en bucle después de setup()
void loop() {
  digitalWrite(ledPin1, HIGH);   // Enciende el primer LED
  digitalWrite(ledPin2, HIGH);   // Enciende el segundo LED
  delay(1000);                   // Mantén los LEDs encendidos por un segundo

  digitalWrite(ledPin1, LOW);    // Apaga el primer LED
  digitalWrite(ledPin2, LOW);    // Apaga el segundo LED
  delay(1000);                   // Espera un segundo
}
