//e6uuj  m                                                                                                                                         /  Square wave generator with PWM and FM
// by F. Sepulveda
// 12/12/2015 - last updated on 12/7/2017

#include "math.h"

/*  mapping board pins 2-13 to user fingers
 *  2 = rigth thumb;  3 R_index; 4-6 other right fingers
 *  7 = left thumb; 8-13 other left fingers
 */

int del_ms; //ms delay
int freq_p2, freq_p3, freq_p4, freq_p5, freq_p6;
int freq_p7, freq_p8, freq_p9, freq_p10, freq_p13;
int del_ON_p2, del_ON_p3, del_ON_p4, del_ON_p5, del_ON_p6; //us delay for ON phase
int del_ON_p7, del_ON_p8, del_ON_p9, del_ON_p10, del_ON_p13;
int del_OFF_p2, del_OFF_p3, del_OFF_p4, del_OFF_p5, del_OFF_p6; //us delay for OFF phase
int del_OFF_p7, del_OFF_p8, del_OFF_p9, del_OFF_p10, del_OFF_p13;

int maxLoops;
int dcycle; // duty cycle
//int pNum = 13; // pin to be tested 

void clearInputserial()
{
  delay(500);
  while (Serial.available()) Serial.read();
}

static inline void pinOutput(int pin, int val)
{
  if (val)
    g_APinDescription[pin].pPort->PIO_SODR = g_APinDescription[pin].ulPin;
    //PORTB |= _BV(PB25);
  else
    g_APinDescription[pin].pPort->PIO_CODR = g_APinDescription[pin].ulPin;
    //PORTB &= ~_BV(PB25);
}

void setup()
{
  int incomingByte = 0;   // for incoming serial datau
  float errorFactor = 1.0; // output freq. error, 1=no error
  int ONpwError;// = 2; // us error with 20 GPIO
  int OFFpwError;// = 9;
  int ideal_pw_13;

  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);pinMode(4,OUTPUT);pinMode(5,OUTPUT);pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);pinMode(8,OUTPUT);pinMode(9,OUTPUT);pinMode(10,OUTPUT);pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);pinMode(13,OUTPUT);
  //;pinMode(pNum, OUTPUT);
  pinOutput(2, 0);
  pinOutput(3, 0);  pinOutput(4, 0);  pinOutput(5, 0);  pinOutput(6, 0);  pinOutput(7, 0);
  pinOutput(8, 0);  pinOutput(9, 0);  pinOutput(10, 0);  pinOutput(10, 0);  pinOutput(11, 0);
  pinOutput(12, 0);  pinOutput(13, 0);
  //pinOutput(pNum, 0);
  
  Serial.begin(115200);
  //delay(3000);
  Serial.println("ON Pulsewidth p13 [us]? ");      //Prompt User for input
  while (Serial.available() == 0)  {  }
  ideal_pw_13 = Serial.parseInt();
  
  //delay(3000);
  clearInputserial();
  Serial.println("Frequency p13 [Hz]? ");      //Prompt User for input
  while (Serial.available() == 0)  {  }
  freq_p13 = Serial.parseInt();

  clearInputserial();
  Serial.print("Ideal ON PW: "); Serial.print(ideal_pw_13); Serial.println(" us");
  Serial.print("Ideal Freq.: "); Serial.print(freq_p13); Serial.println(" Hz");
  delay(500);

  // calculate delta_us_ON and delta_us_OFF ---> not assuming duty_cycle=50%
  del_ON_p13 = (int) (ideal_pw_13 * 0.75 - 1); // ON_PW error correction 
  
  
  int period_p13 = (int) (1e6 / freq_p13); // Ideal period in us
  int i_off_13 = period_p13 - ideal_pw_13;
  Serial.print("Ideal OFF PW : "); Serial.print(i_off_13); Serial.println(" us");
  
  del_OFF_p13 = (int) (0.9*i_off_13);  // OFF PW error correction
  Serial.print("Sent ON PW : "); Serial.print(del_ON_p13); Serial.println(" us");
  Serial.print("Sent OFF PW: "); Serial.print(del_OFF_p13); Serial.println(" us");

  maxLoops = freq_p13 * 60; // 10s of test signal
  Serial.print("maxLoops: "); Serial.println(maxLoops);
  delay(1000); // delay to wait for serial buffer to finish sending
}

// ***************************************************************
// ***************************************************************

void loop()
{
  int Loopcount = maxLoops;
  //int Loopcount=4;
  //int dd=1000;
  //Serial.print("maxLoops: ");Serial.println(Loopcount);
  //delay(500); // delay to wait for serial buffer to finish sending

  //noInterrupts();
 while (--Loopcount)
  { // for now, same output on all pins
    pinOutput(2,1);
    pinOutput(3, 1);
    pinOutput(4, 1);
    pinOutput(5, 1);
    pinOutput(6, 1);
    pinOutput(7, 1);
    pinOutput(8, 1);
    pinOutput(9, 1);
    pinOutput(10, 1);
    pinOutput(11, 1);
    pinOutput(12, 1);
    pinOutput(13, 1);
/*    pinOutput(22, 1);
    pinOutput(23, 1);
    pinOutput(24, 1);
    pinOutput(25, 1);
    pinOutput(26, 1);
    pinOutput(27, 1);
    pinOutput(28, 1);
    pinOutput(29, 1);
    pinOutput(30, 1);*/
   // pinOutput(pNum, 1);
    delayMicroseconds(del_ON_p13);

    pinOutput(2,0);
    pinOutput(3, 0);
    pinOutput(4, 0);
    pinOutput(5, 0);
    pinOutput(6, 0);
    pinOutput(7, 0);
    pinOutput(8, 0);
    pinOutput(9, 0);
    pinOutput(10, 0);
    pinOutput(10, 0);
    pinOutput(11, 0);
    pinOutput(12, 0);
    pinOutput(13, 0);
   /* pinOutput(22, 0);
    pinOutput(23, 0);
    pinOutput(24, 0);
    pinOutput(25, 0);
    pinOutput(26, 0);
    pinOutput(27, 0);
    pinOutput(28, 0);
    pinOutput(29, 0);
    pinOutput(30, 0);*/
    //pinOutput(pNum, 0);
    delayMicroseconds(del_OFF_p13);
  }

  //interrupts();
  pinOutput(2,0);
  pinOutput(3, 0);
  pinOutput(4, 0);
  pinOutput(5, 0);
  pinOutput(6, 0);
  pinOutput(7, 0);
  pinOutput(8, 0);
  pinOutput(9, 0);
  pinOutput(10, 0);
  pinOutput(10, 0);
  pinOutput(11, 0);
  pinOutput(12, 0);
  pinOutput(13, 0);
  /*pinOutput(22, 0);
  pinOutput(23, 0);
  pinOutput(24, 0);
  pinOutput(25, 0);
  pinOutput(26, 0);
  pinOutput(27, 0);
  pinOutput(28, 0);
  pinOutput(29, 0);
  pinOutput(30, 0);*/
  //pinOutput(pNum, 0);

  //pinMode(pNum, INPUT);
  Serial.println("End of program");
  delay(500);

  exit(0);

}
