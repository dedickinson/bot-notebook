#include "pitches.h";

int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};
 
void setup() 
{ 
  for (int rpt = 0; rpt <5; rpt++) {
    for (int note = 0; note < 8; note++) {
      int noteDuration = 1000/noteDurations[note];
      tone(8, melody[note], noteDuration);
      
      delay(noteDuration * 1.30);
      
      noTone(8);
    }
    delay(100);
  }
} 
 
 
void loop() 
{ 

} 

