int potPin = A0; // Pin analógico al que está conectado el potenciómetro
int ledPin1 = 10; // Pin digital al que está conectado el primer LED
int ledPin2 = 11; // Pin digital al que está conectado el segundo LED
int ledPin3 = 12; // Pin digital al que está conectado el tercer LED

void setup() {
  pinMode(ledPin1, OUTPUT); // Configura el pin del primer LED como salida
  pinMode(ledPin2, OUTPUT); // Configura el pin del segundo LED como salida
  pinMode(ledPin3, OUTPUT); // Configura el pin del tercer LED como salida
  Serial.begin(9600); // Inicializa la comunicación serie
}

void loop() {
  int potValue = analogRead(potPin); // Lee el valor analógico del potenciómetro
  
  Serial.print("Potentiometer Value: ");
  Serial.println(potValue);
  
  if (potValue <= 300) {
    digitalWrite(ledPin1, HIGH); // Enciende el primer LED si el valor es menor o igual a 300
    digitalWrite(ledPin2, LOW); // Apaga el segundo LED
    digitalWrite(ledPin3, LOW); // Apaga el tercer LED
  } else if (potValue > 300 && potValue < 600) {
    digitalWrite(ledPin1, LOW); // Apaga el primer LED
    digitalWrite(ledPin2, HIGH); // Enciende el segundo LED si el valor está entre 300 y 600
    digitalWrite(ledPin3, LOW); // Apaga el tercer LED
  } else if (potValue >= 600) {
    digitalWrite(ledPin1, LOW); // Apaga el primer LED
    digitalWrite(ledPin2, LOW); // Apaga el segundo LED
    digitalWrite(ledPin3, HIGH); // Enciende el tercer LED si el valor es igual o superior a 600
  }
  
  delay(100); // Pequeño retardo para estabilidad
}
