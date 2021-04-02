#include <SoftwareSerial.h>
const int analogPorts[] = {A0,A1,A2,A3,A4,A5};

void setup() 
{
  Serial.begin(9600);

}

void loop() 
{
  for(int i = 0; i<sizeof(analogPorts)/sizeof(analogPorts[0]);i++)
  {
    Serial.println("a" + String(i) +": " + analogRead(analogPorts[i]));
  }
  delay(100); // delay has to be the same as the RPI4
  Serial.flush();
}
