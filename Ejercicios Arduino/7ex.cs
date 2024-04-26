// Define los pines de los LEDs y del pulsador
int ledPin1 = 9;
int ledPin2 = 10;
int buttonPin = 2;

// Variables para almacenar el estado del pulsador
int buttonState = 0;
int lastButtonState = 0;

// Variables para controlar cuál LED está activo
bool led1Active = true;

void setup() {
  // Configura los pines de los LEDs como salida y el del pulsador como entrada
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(buttonPin, INPUT);

  // Inicializa los LEDs apagados
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
}

void loop() {
  // Lee el estado del pulsador
  int reading = digitalRead(buttonPin);

  // Si el estado del pulsador cambia a presionado, cambia el LED activo
  if (reading != lastButtonState) {
    if (reading == HIGH) {
      led1Active = !led1Active; // Cambia entre verdadero y falso
    }
    delay(50); // Debounce delay
  }

  // Actualiza el estado del pulsador para la próxima lectura
  lastButtonState = reading;

  // Enciende el LED activo y apaga el otro
  digitalWrite(ledPin1, led1Active ? HIGH : LOW);
  digitalWrite(ledPin2, !led1Active ? HIGH : LOW);
}

