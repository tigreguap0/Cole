// Define los pines para los colores del LED RGB
int redPin = 9;
int greenPin = 10;
int bluePin = 11;

void setup() {
  // Configura los pines como salida
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  // Enciende el color rojo
  setColor(HIGH, LOW, LOW);
  delay(1000); // Espera un segundo
  
  // Enciende el color verde
  setColor(LOW, HIGH, LOW);
  delay(1000); // Espera un segundo
  
  // Enciende el color azul
  setColor(LOW, LOW, HIGH);
  delay(1000); // Espera un segundo
  
  // Apaga el LED
  setColor(LOW, LOW, LOW);
  delay(1000); // Espera un segundo
}

// Función para establecer el color del LED RGB
void setColor(bool red, bool green, bool blue) {
  digitalWrite(redPin, red);
  digitalWrite(greenPin, green);
  digitalWrite(bluePin, blue);
}
