// Define el pin donde se conecta el LED
int ledPin = 13;                

// La función setup() se ejecuta una vez cuando se reinicia o se enciende la placa
void setup() {
  // Configura el pin del LED como salida
  pinMode(ledPin, OUTPUT);     
}

// La función loop() se ejecuta continuamente en bucle después de setup()
void loop() {
  digitalWrite(ledPin, HIGH);   // Enciende el LED
  delay(1000);                  // Espera un segundo (1000 milisegundos)
  digitalWrite(ledPin, LOW);    // Apaga el LED
  delay(1000);                  // Espera otro segundo
}
