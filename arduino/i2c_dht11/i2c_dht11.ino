// Based on http://playground.arduino.cc/Main/DHT11Lib
// Requires dht11.h and dht11.cpp to be copied into the libraries folder

#include <Wire.h>
#include <dht11.h>

// The Arduino GPIO pin:
#define DHT11PIN 8

// The agent's I2C address
#define I2C_AGENT_ADDRESS 0x15


enum dht11_return_code {
  OK = DHTLIB_OK,
  ERROR_CHECKSUM = DHTLIB_ERROR_CHECKSUM,
  ERROR_TIMEOUT = DHTLIB_ERROR_TIMEOUT,
  NOT_READ = -10
};

typedef struct sensor_data_type {
  int read_status;
  int temperature;
  int humidity;
};

typedef union i2c_sensor_packet_type {
  sensor_data_type sensor_data;
  byte packet_data[sizeof(sensor_data_type)];
};

#define PACKET_SIZE sizeof(sensor_data_type)

dht11 sensor_dht11;
sensor_data_type sensor_data;

void setup()
{ 
  sensor_data.read_status = NOT_READ;
  sensor_data.temperature = -1000;
  sensor_data.humidity = -1000;  
  
  Wire.begin(I2C_AGENT_ADDRESS);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  Serial.println(PACKET_SIZE);
}

void loop(){
  sensor_data.read_status = sensor_dht11.read(DHT11PIN);
  
  if (sensor_data.read_status == OK) {
    sensor_data.temperature = sensor_dht11.temperature;
    sensor_data.humidity = sensor_dht11.humidity;
  } else {
    sensor_data.temperature = -1000;
    sensor_data.humidity = -1000;
  }
  
  delay(5000);
}

void receiveEvent(int bytes) {
  //Serial.print("Receive event received: ");
  
  while (Wire.available()) {
    int val = Wire.read();
    //Serial.print(val);
  }
  
  //Serial.println();
}

void requestEvent() {
  //Serial.println("request event received");
  i2c_sensor_packet_type packet;
  packet.sensor_data = sensor_data;
  
  Wire.write(packet.packet_data, PACKET_SIZE);

}


