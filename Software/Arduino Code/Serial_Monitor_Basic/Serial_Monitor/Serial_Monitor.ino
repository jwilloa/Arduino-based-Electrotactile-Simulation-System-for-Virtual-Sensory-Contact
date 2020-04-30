/*
  Serial Monitor

  Arduino boards turns on an LED when it receives the character
  'H', and turns off the LED when it receives the character 'L'.

  The data is received to the Arduino Serial Monitor, via a Python script.

  The circuit:
  - LED connected from digital pin 13 to ground

*/


// the pin that the LED is attached to
const int ledPinThumb = 13;
const int ledPinIndex = 12;
const int ledPinMiddle = 11;
const int ledPinRing = 7;
const int ledPinLittle = 6;

int incomingByte;      // a variable to read incoming serial data into

void setup() {
  
  // initialize serial communication:
  Serial.begin(9600);
  
  // initialize the LED pin as an output:
  pinMode(ledPinThumb, OUTPUT);
//  pinMode(ledPinIndex, OUTPUT);
//  pinMode(ledPinMiddle, OUTPUT);
//  pinMode(ledPinRing, OUTPUT);
//  pinMode(ledPinLittle, OUTPUT);     
}

void loop() {
  
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H, turn on the LED:
    
    if (incomingByte == 'T') {
      digitalWrite(ledPinThumb, HIGH);
      }
//    if (incomingByte == 'I') {
//      digitalWrite(ledPinIndex, HIGH);
//      }
//    if (incomingByte == 'M') {     
//      digitalWrite(ledPinMiddle, HIGH);
//      }
//    if (incomingByte == 'R') {
//      digitalWrite(ledPinRing, HIGH);
//      }
//    if (incomingByte == 'S') {
//      digitalWrite(ledPinLittle, HIGH);
//    }
    
    
    // if it's an L, turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPinThumb, LOW);
      }
//    if (incomingByte == 'L') {      
//      digitalWrite(ledPinIndex, LOW);
//      }
//    if (incomingByte == 'L') {
//      digitalWrite(ledPinMiddle, LOW);
//      }
//    if (incomingByte == 'L') {
//      digitalWrite(ledPinRing, LOW);
//      }
//    if (incomingByte == 'L') {
//      digitalWrite(ledPinLittle, LOW);
//    }
  }
}
