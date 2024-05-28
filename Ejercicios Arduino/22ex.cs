int potPin = A0; // Pin analógico al que está conectado el potenciómetro
int ledPin = 13; // Pin digital al que está conectado el LED

void setup() {
  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int potValue = analogRead(potPin); // Lee el valor analógico del potenciómetro
  int delayTime = map(potValue, 0, 1023, 100, 2000); // Mapea el valor leído a un rango de tiempo de retardo
  
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" - Delay Time: ");
  Serial.println(delayTime);
  
  digitalWrite(ledPin, HIGH); // Enciende el LED
  delay(delayTime); // Espera por el tiempo mapeado
  digitalWrite(ledPin, LOW); // Apaga el LED
  delay(delayTime); // Espera por el tiempo mapeado
}
