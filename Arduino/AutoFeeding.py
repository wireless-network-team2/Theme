#include <Servo.h>

const int ServoPin = 10; //서보모터 핀
const int LittlePin = 5; //버튼 핀
const int HalfPin = 6;
const int FullPin = 7;
int Pos = 0; //서보모터 각도 설정

Servo myservo;

void setup() {
  myservo.attach(ServoPin);
  myservo.write(Pos);
  
  pinMode(LittlePin, INPUT);
  pinMode(HalfPin, INPUT);
  pinMode(FullPin, INPUT);
}

void loop() {
  if(digitalRead(LittlePin) == HIGH){ //버튼이 눌렸는지 확인
    Pos = 30; //서보모터 각도 지정
    myservo.write(Pos); //서보모터 제어
    delay(1000); 
    Pos = 0; //서보모터 각도 초기값으로 지정 
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
