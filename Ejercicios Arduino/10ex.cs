// Define los pines para los LEDs
int redPin = 9;       // Pin para el LED rojo
int yellowPin = 10;   // Pin para el LED amarillo
int greenPin = 11;    // Pin para el LED verde

void setup() {
  // Configura los pines como salida
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  // LED Rojo
  controlTrafficLight(redPin, 5000, 3000);
  
  // LED Amarillo
  controlTrafficLight(yellowPin, 5000, 3000);
  
  // LED Verde
  controlTrafficLight(greenPin, 5000, 3000);
}

void controlTrafficLight(int pin, int onTime, int blinkTime) {
  digitalWrite(pin, HIGH);   // Enciende el LED
  delay(onTime);             // Mantén el LED encendido por 'onTime' milisegundos

  // Hacer parpadear el LED durante 'blinkTime' milisegundos
  long endTime = millis() + blinkTime;
  while (millis() < endTime) {
    digitalWrite(pin, LOW);
    delay(500);
    digitalWrite(pin, HIGH);
    delay(500);
  }

  digitalWrite(pin, LOW);    // Apaga el LED
  delay(1000);               // Pequeña pausa antes de cambiar al siguiente LED
}

