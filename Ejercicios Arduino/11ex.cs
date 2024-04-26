void setup() {
  // Inicia la comunicación serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Lee el valor analógico del pin A0 (potenciómetro)
  int sensorValue = analogRead(A0);

  // Envía el valor leído a la consola del IDE de Arduino
  Serial.println(sensorValue);

  // Espera un poco antes de la próxima lectura
  delay(500);
}
