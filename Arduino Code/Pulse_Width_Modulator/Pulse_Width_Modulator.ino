/*
  Fading

  This example shows how to fade an LED using the analogWrite() function.

  The circuit:
  - LED attached from digital pin 9 to ground.

  created 1 Nov 2008
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Fading
*/

int led0 = 13;
int led1 = 12;
int led2 = 11;
int led3 = 7;
int led4 = 6; 

void setup() {
  // nothing happens in setup
}

void loop() {
  // fade in from min to max in increments of 5 points:
  for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
    // sets the value (range from 0 to 255):
    analogWrite(led0, fadeValue);
    analogWrite(led1, fadeValue);
    analogWrite(led2, fadeValue);
    analogWrite(led3, fadeValue);
    analogWrite(led4, fadeValue);
    // wait for 30 milliseconds to see the dimming effect
    delay(30);
  }

  // fade out from max to min in increments of 5 points:
  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // sets the value (range from 0 to 255):
    analogWrite(led0, fadeValue);
    analogWrite(led1, fadeValue);
    analogWrite(led2, fadeValue);
    analogWrite(led3, fadeValue);
    analogWrite(led4, fadeValue);
    // wait for 30 milliseconds to see the dimming effect
    delay(30);
  }
}
