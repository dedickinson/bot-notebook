#include <Wire.h>

#define I2C_AGENT_ADDRESS 0x04


void setup() {
 
  Wire.begin(I2C_AGENT_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.begin(9600);
  
}

void loop() {

}



void receiveData(int byteCount) {
  while(Wire.available()) {
    int inputVal = Wire.read();
    Serial.print("I2C received: ");
    Serial.println(inputVal);
  }
}

void sendData() {
  int outputVal = random(99);
  Wire.write(outputVal);
  Serial.print("Output: ");
  Serial.println(outputVal);
}
