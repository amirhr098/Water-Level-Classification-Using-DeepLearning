#include <Servo.h>
int value;
int Relay1 = 8;
Servo servo1;
Servo servo2;
char input;
void setup() 
{ 
servo1.attach(10);
servo2.attach(9);
Serial.begin(9600);
pinMode (Relay1,OUTPUT);
} 

void loop() 
{ 
  
  if (Serial.available())
  {input = Serial.read();}
  if (input=='A')
  {
servo1.write(80);
servo2.write(90);
  }
  if (input=='B')
  {
servo1.write(80);
servo2.write(35);
  }
  if (input=='C')
  {
servo1.write(35);
servo2.write(35);
  }
  if (input=='0')
  {digitalWrite(Relay1,HIGH);
  }
   if (input=='1')
  {digitalWrite(Relay1,LOW);
  }
  
} 
