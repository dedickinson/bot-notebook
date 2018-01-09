#include "pitches.h";

const int INPUT_PIN_PIR = 7;
const int OUTPUT_PIN_BUZZER = 8;
const int OUTPUT_PIN_LED = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(INPUT_PIN_PIR, INPUT);
  // pinMode(OUTPUT_PIN_BUZZER, OUTPUT);
  pinMode(OUTPUT_PIN_LED, OUTPUT);
  
  digitalWrite(OUTPUT_PIN_LED, LOW);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(OUTPUT_PIN_LED, LOW); 
  int reading = digitalRead(INPUT_PIN_PIR);
  Serial.println(reading);
  
  if (reading) {
    digitalWrite(OUTPUT_PIN_LED, HIGH);
    playToneAlert();
    digitalWrite(OUTPUT_PIN_LED, LOW);
  }
  
  delay(500);
}

const int melody[] = {
  NOTE_C4, NOTE_G3
};

const int NOTE_DURATION = 1000/4;

void playToneAlert() {
  for (int note = 0; note < sizeof(melody); note++) {
    
    tone(OUTPUT_PIN_BUZZER, melody[note], NOTE_DURATION);
    delay(NOTE_DURATION * 1.30);
    //noTone(8);
  }
}
