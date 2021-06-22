#include <SoftwareSerial.h>
const int analogPorts[] = {A0,A1,A2,A3,A4,A5};
const int ports = sizeof(analogPorts)/sizeof(analogPorts[0]);
const int trigger = 12;
const int echo = 11;

void setup() 
{
  Serial.begin(9600);
  pinMode (trigger, OUTPUT);
  pinMode (echo, INPUT);
}

void loop() 
{
  for(int i = 0; i<ports;i++)
  {
    //Serial.println("a" + String(i) +": " + analogRead(analogPorts[i]));
  }
  Serial.println("a"+ String(ports) +": " + getDistance());
  delay(100); // delay has to be the same as the RPI4
  Serial.flush();
}

float getDistance()
{
  double distance;
  long duration;
  //At the beginning, the trigger must be set low 
  digitalWrite(trigger, LOW);
  delayMicroseconds (2);

  digitalWrite(trigger, HIGH);
  delayMicroseconds (10);
  digitalWrite(trigger, LOW);

  //pulseIn function reads if a pin is either high or low
  //echo pin outputs the time it took the wave to hit the object and comeback in microseconds (us)
  duration = pulseIn (echo, HIGH);

  //Speed of sound = 340m/s or 0.034cm/us  
  //Distance will be in cm 1
  distance = duration * 0.034/2*10;
  return distance;
}
