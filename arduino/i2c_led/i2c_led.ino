#include <Wire.h>

// Based on https://github.com/simonmonk/raspberrypi_cookbook/blob/master/code/ArduinoI2C/ArduinoI2C.ino

int DEVICE_ADDRESS = 0x04;
int ledPin = 13;

void setup() 
{
    pinMode(ledPin, OUTPUT);
    
    Wire.begin(DEVICE_ADDRESS);
    Wire.onReceive(receiveRequest);
    Serial.begin(9600);
}

void loop()
{
}

void receiveRequest(int n)
{
  Serial.println("Request received");
  char val = Wire.read();
  digitalWrite(ledPin, val);
}


