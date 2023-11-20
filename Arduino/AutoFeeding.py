#include <Servo.h>

const int ServoPin = 10;
const int LittlePin = 5;
const int HalfPin = 6;
const int FullPin = 7;
int Pos = 0;

Servo myservo;

void setup() {
  myservo.attach(ServoPin);
  myservo.write(0);
  
  pinMode(LittlePin, INPUT);
  pinMode(HalfPin, INPUT);
  pinMode(FullPin, INPUT);
}

void loop() {
  if(digitalRead(LittlePin) == HIGH){
    Pos = 30;
    myservo.write(Pos);
    delay(1000);
    Pos = 0;
    myservo.write(Pos);
  }
  else if(digitalRead(HalfPin) == HIGH) {
    Pos = 60;
    myservo.write(Pos);
    delay(1000);
    Pos = 0;
    myservo.write(Pos);
  }else if(digitalRead(FullPin) == HIGH) {
    Pos = 90;
    myservo.write(Pos);
    delay(1000);
    Pos = 0;
    myservo.write(Pos);
  }
}
