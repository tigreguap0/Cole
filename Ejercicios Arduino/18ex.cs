int ldrPin = A0; // Pin analógico al que está conectado la fotorresistencia (LDR)
int ledPin1 = 13; // Pin digital al que está conectado el primer LED
int ledPin2 = 12; // Pin digital al que está conectado el segundo LED
int buzzerPin = 11; // Pin digital al que está conectado el buzzer

void setup() {
  pinMode(ledPin1, OUTPUT); // Configura el pin del primer LED como salida
  pinMode(ledPin2, OUTPUT); // Configura el pin del segundo LED como salida
  pinMode(buzzerPin, OUTPUT); // Configura el pin del buzzer como salida
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int ldrValue = analogRead(ldrPin); // Lee el valor analógico de la fotorresistencia
  
  Serial.print("LDR Value: ");
  Serial.println(ldrValue);
  
  if (ldrValue < 200) {
    digitalWrite(ledPin1, HIGH); // Enciende el primer LED si el valor es menor que 200
    digitalWrite(ledPin2, LOW); // Apaga el segundo LED
    digitalWrite(buzzerPin, LOW); // Apaga el buzzer
  } else if (ldrValue >= 200 && ldrValue < 300) {
    digitalWrite(ledPin1, HIGH); // Enciende el primer LED
    digitalWrite(ledPin2, HIGH); // Enciende el segundo LED si el valor está entre 200 y 300
    digitalWrite(buzzerPin, LOW); // Apaga el buzzer
  } else if (ldrValue >= 300) {
    digitalWrite(ledPin1, LOW); // Apaga el primer LED
    digitalWrite(ledPin2, LOW); // Apaga el segundo LED
    digitalWrite(buzzerPin, HIGH); // Enciende el buzzer si el valor es igual o superior a 300
  }
  
  delay(1000); // Espera 1 segundo antes de realizar la siguiente lectura
}
