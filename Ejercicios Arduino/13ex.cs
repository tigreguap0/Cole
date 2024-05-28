#include <Arduino.h>

// Pines para los LEDs y botones
const int ledPins[] = {2, 3, 4, 5};
const int buttonPins[] = {6, 7, 8, 9};
const int numButtons = 4;

// Variables para el control del juego
int gameSequence[100];  // Almacena hasta 100 pasos en la secuencia
int stepCount = 0;      // Cantidad de pasos en la secuencia actual
int inputIndex = 0;     // Índice para la entrada del jugador

void setup() {
  for (int i = 0; i < numButtons; i++) {
    pinMode(ledPins[i], OUTPUT);
    pinMode(buttonPins[i], INPUT);
  }
  randomSeed(analogRead(0));  // Inicializa la semilla aleatoria
}

void loop() {
  playSequence();  // Reproduce la secuencia actual con los LEDs
  if (readPlayerInput()) {  // Lee y compara la entrada del jugador
    stepCount++;  // Avanza a la siguiente ronda si el jugador tiene éxito
    delay(1000);  // Breve pausa antes de la siguiente secuencia
  } else {
    gameOver();  // El jugador falla y el juego termina
  }
}

void playSequence() {
  for (int i = 0; i < stepCount; i++) {
    digitalWrite(ledPins[gameSequence[i]], HIGH);
    delay(600);
    digitalWrite(ledPins[gameSequence[i]], LOW);
    delay(400);
  }
}

bool readPlayerInput() {
  for (int i = 0; i < stepCount; i++) {
    int buttonState;
    do {
      buttonState = checkButtons();  // Espera hasta que un botón sea presionado
    } while (buttonState == -1);

    if (buttonState != gameSequence[i]) {
      return false;  // Error en la secuencia
    }
    delay(400);  // Breve pausa entre entradas
  }
  return true;
}

int checkButtons() {
  for (int i = 0; i < numButtons; i++) {
    if (digitalRead(buttonPins[i]) == HIGH) {
      lightButton(i);  // Enciende el LED correspondiente al botón presionado
      delay(200);
      digitalWrite(ledPins[i], LOW);
      return i;
    }
  }
  return -1;  // Ningún botón presionado
}

void lightButton(int button) {
  digitalWrite(ledPins[button], HIGH);
  delay(400);
  digitalWrite(ledPins[button], LOW);
}

void gameOver() {
  // Indica el final del juego
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], HIGH);
  }
  delay(1000);
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], LOW);
  }
  delay(1000);
  stepCount = 0;  // Reinicia el juego
  for (int i = 0; i < 100; i++) {
    gameSequence[i] = random(numButtons);  // Genera una nueva secuencia para el siguiente juego
  }
}
