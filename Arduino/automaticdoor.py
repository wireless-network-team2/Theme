#include <Servo.h>

Servo myservo;

int ServoPin = 10; //서보모터 핀
int trigPin = 13; // 트리그 핀(초음파 센서 송신부)
int echoPin = 12; // 에코 핀 (초음파 센서 수신부)
float duration = 0, distance = 0; //초음파 센서를 통한 주기 및 거리 측정
int Pos = 0; // 서보 모터 각도 설정

void setup() {
  pinMode(tirgPin, OUTPUT); 
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalwrite(trigPin, HIGH); // 초음파 발생하여 주기 측정
  delay(10);
  digitalwrite(trigPin, LOW);	
  
  duration = pulseln(echoPim, HIGH);// pulseIn() 함수를 이용한 초음파 센서 주기 (ms) 반환
  distance = ((float)(340 * duration)) / 10000 / 2; //cm 단위로 거리 변경
  
  if(distance < 15){ //거리가 15cm 미만일떄
    myservo.attach(ServoPin);
    Pos = 90;
    myservo.write(Pos); // 서보모터 제어
    delay(1000);
    Pos = 0;
    myservo.write(Pos);
    delay(1000);
    myservo.detach();
  }
  else{
    delay(1000);
  }
}

//pulseln() 핀으로 입력되는 펄스의 시간을 측정하는 함수
