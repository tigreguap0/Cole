// Define el pin donde se conecta el LED
int ledPin = 13;               

// Tiempo inicial de espera en milisegundos
float delayTime = 5000;        

// La función setup() se ejecuta una vez cuando se reinicia o se enciende la placa
void setup() {
  // Configura el pin del LED como salida
  pinMode(ledPin, OUTPUT);     
}

// La función loop() se ejecuta continuamente en bucle después de setup()
void loop() {
  digitalWrite(ledPin, HIGH);   // Enciende el LED
  delay((int)delayTime);        // Espera el tiempo definido en delayTime
  digitalWrite(ledPin, LOW);    // Apaga el LED
  delay((int)delayTime);        // Espera el tiempo definido en delayTime
  
  delayTime -= 500;             // Reduce el tiempo de espera en 500 milisegundos (medio segundo)

  if (delayTime <= 0) {         // Cuando el tiempo de espera llega a 0 o menos
    digitalWrite(ledPin, HIGH); // Enciende el LED permanentemente
    while(1);                   // Bucle infinito para detener más ejecuciones
  }
}
