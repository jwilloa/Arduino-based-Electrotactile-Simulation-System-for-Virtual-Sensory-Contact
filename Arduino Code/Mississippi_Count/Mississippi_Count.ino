#define LED 8
int cnt=0;
void setup() {
 
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  
}

void loop() {
//  digitalWrite(LED, HIGH);
 // delay(1000);
 // digitalWrite(LED, LOW);
 // delay(1000);
  Serial.print("I am Counting to: ");
  Serial.print(cnt);
  Serial.println(" Mississippi.");
  cnt=cnt+1;
  delay(1000);
  
}
