int ldrPin = A0; // Pin analógico al que está conectado la fotorresistencia (LDR)

void setup() {
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int ldrValue = analogRead(ldrPin); // Lee el valor analógico de la fotorresistencia
  float voltage = ldrValue * (5.0 / 1023.0); // Convierte el valor leído a tensión
  
  Serial.print("LDR Value: ");
  Serial.print(ldrValue);
  Serial.print(" - Voltage: ");
  Serial.println(voltage);
  
  delay(1000); // Espera 1 segundo antes de realizar la siguiente lectura
}
