int ldrPin = A0; // Pin analógico al que está conectado la fotorresistencia (LDR)
int ledPin = 13; // Pin digital al que está conectado el LED

void setup() {
  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int ldrValue = analogRead(ldrPin); // Lee el valor analógico de la fotorresistencia
  
  Serial.print("LDR Value: ");
  Serial.println(ldrValue);
  
  if (ldrValue <= 200) {
    digitalWrite(ledPin, HIGH); // Enciende el LED si el valor es menor o igual a 200
  } else {
    digitalWrite(ledPin, LOW); // Apaga el LED si el valor es mayor a 200
  }
  
  delay(1000); // Espera 1 segundo antes de realizar la siguiente lectura
}
