// Define los pines para los colores del LED RGB
int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int buttonPin = 2;  // Pin conectado al pulsador

void setup() {
  // Configura los pines como salida
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);  // Configura el pin del pulsador con pull-up interno
}

void loop() {
  // Comprueba si el botón ha sido presionado
  if (digitalRead(buttonPin) == LOW) {  // El botón está conectado a tierra cuando se presiona
    // Enciende el color rojo y mantenlo por tres segundos
    setColor(HIGH, LOW, LOW);
    delay(3000);  // Espera tres segundos
  }

  // Secuencia normal de colores cada uno por un segundo
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
