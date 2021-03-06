#include <SoftwareSerial.h>


void setup() 
{
  Serial.begin(9600);

}
void loop() 
{
  Serial.print("a0: ");
  Serial.println(1);
  Serial.print("a1: ");
  Serial.println(20);
  Serial.print("a2: ");
  Serial.println(300);
  Serial.print("a3: ");
  Serial.println(4000);
  Serial.print("a4: ");
  Serial.println(599);
  Serial.print("a5: ");
  Serial.println(0);
  delay(100);
  Serial.flush();
}
