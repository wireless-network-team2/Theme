// 아두이노에 pH 센서가 연결된 경우를 가정한 코드 예제

const int analogPin = A0; // pH 센서가 연결된 아날로그 핀
float voltage; //전압
float pHValue; //pH값

void setup() {
  Serial.begin(9600);  // 시리얼 통신 시작
}

void loop() {
  // 아날로그 핀에서 값을 읽음
  int rawValue = analogRead(analogPin);

  // 아날로그 값을 전압으로 변환
  voltage = (rawValue / 1024.0) * 5.0;

  // 전압을 pH 값으로 변환 (이 부분은 pH 센서의 특정 데이터시트에 따라 달라질 수 있음)
  pHValue = pHValue = 7 - (voltage - VOffset);  /* 여기에 전압을 pH로 변환하는 수식을 추가하세요 */;

  // 결과를 시리얼 모니터에 출력
  Serial.print("Raw Value: ");
  Serial.print(rawValue);
  Serial.print("\tVoltage: ");
  Serial.print(voltage);
  Serial.print("\tpH Value: ");
  Serial.println(pHValue);

  delay(1000); // 1초 동안 대기
}
