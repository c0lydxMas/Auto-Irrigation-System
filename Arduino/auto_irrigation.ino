#include "SerialTransfer.h"

#define pin_analog A0
#define pin_digital 3
#define pin_led 13
#define pin_relay 12
#define moisture_threshhold 1300

SerialTransfer myTransfer;

void setup() 
{
  Serial.begin(9600);

  pinMode (pin_analog, INPUT);
  pinMode(pin_digital, INPUT);
  pinMode (pin_led, OUTPUT);
  pinMode (pin_relay, OUTPUT);
  
}
 
void loop() 
{
  // Read the voltage value from the soil moisture sensor
  // The module came with the sensor helps converting analog
  // signal from the sensor to an integer ranged from 0 to 1024
  // 0: moistest - 1024: driest
  // Read sensor value from A0 pin
  int soil_moisture = analogRead(pin_analog);

  // Write data to serial port
  Serial.println(soil_moisture);

  // If soil moisture pass the predefined value, turn on the LED
  // and activate the relay
  if(soil_moisture > moisture_threshhold)
  {
    // Dry soil, high moisture value
    // Turn on the LED
    digitalWrite(pin_led,HIGH);
    // Activate the relay
    digitalWrite(pin_relay, LOW);
  }
  else
  {
    // Enough moisture, low moisture value
    // Turn off the LED
    digitalWrite(pin_led, LOW);
    // Deactivate the relay
    digitalWrite(pin_relay, HIGH);
  }
}
