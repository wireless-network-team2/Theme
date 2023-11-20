void setup(){
  pinMode(4,OUTPUT);                 //핀 4번을 출력으로
  Serial.begin(9600);                //시리얼통신설정

}

void loop(){

  int a = analogRead(A0);            //data변수에 조도 센서 측정값 저장

  delay(200);
  if(a>300)digitalWrite(4,LOW);      //a가 300이 넘으면 4번핀에 LOW값
  else digitalWrite(4,HIGH);         //a가 300이 안넘으면 4번핀에 HIGH값

  Serial.println(a);                 //측정값에 따라 나온 결과값 출력
}