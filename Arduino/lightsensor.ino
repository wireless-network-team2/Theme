void setup() 
{
 pinMode(13, OUTPUT);                     // 디지털 13번핀을 출력모드로 설정
 Serial.begin(9600);
}

void loop()
{
  int readValue = analogRead(A0);         //조도센서에서 읽어들이는 값
  Serial.println(readValue);              //읽어온 센서값 출력

  if(readValue > 500)                     //읽어온 센서값 500 기준점
    digitalWrite(13, HIGH);               //빛이 어두우면 가로등을 킨다.
  else
    digitalWrite(13, LOW);                //빛이 밝으면 가로등을 끈다.
 
}