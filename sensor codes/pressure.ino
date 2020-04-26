
int sensoroutput = 4; // the analog pin connected to the sensor
int THRESHOLD = 1 ;
void setup()
{
   // this function is used to declare led connected pin as output
   Serial.begin(9600);
}
void loop()
{
  int value = analogRead(sensoroutput);  // function to read analog voltage from sensor
  Serial.print(value);
  Serial.print("\n");
  delay(2000);
//  if (value >= THRESHOLD)                    // function to check voltage level from sensor
//  {
//    Serial.print("%d",value);
//    delay(3000); // to make the LED visible
//  } 
//   else
//   {
//    Serial.print("%d",value);
//    Serial.print("bye");
//    delay(2000);
//   }
}
