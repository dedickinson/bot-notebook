// Based on http://playground.arduino.cc/Main/DHT11Lib
// Requires dht11.h and dht11.cpp to be copied into the libraries folder

#include <Wire.h>
#include <dht11.h>

#define DHT11PIN 8
#define I2C_AGENT_ADDRESS 0x04

dht11 DHT11;

void setup()
{
  Wire.begin(I2C_AGENT_ADDRESS);
  Wire.onRequest(sendData);
  Serial.begin(9600);
  Serial.println("DHT11 TEST PROGRAM ");
  Serial.print("LIBRARY VERSION: ");
  Serial.println(DHT11LIB_VERSION);
  Serial.println("--------------------\n");
}

void loop()
{
  delay(5000);
  int chk = DHT11.read(DHT11PIN);
  Serial.print("Read sensor: ");
  switch (chk)
  {
    case DHTLIB_OK: 
		Serial.println("OK"); 
		break;
    case DHTLIB_ERROR_CHECKSUM: 
		Serial.println("Checksum error"); 
		break;
    case DHTLIB_ERROR_TIMEOUT: 
		Serial.println("Time out error"); 
		break;
    default: 
		Serial.println("Unknown error"); 
		break;
  }

  Serial.print("Humidity (%): ");
  Serial.println(DHT11.humidity);

  Serial.print("Temperature: ");
  Serial.println(DHT11.temperature);

  Serial.println("--------------------\n");
}

void sendData() {
  // TODO - get this to work
  float data[2];
  data[0] = (float)DHT11.temperature;
  data[1] = (float)DHT11.humidity;
  Wire.write((byte*) data, 2 * sizeof(float));
}
