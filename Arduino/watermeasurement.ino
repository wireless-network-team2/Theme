#include <LiquidCrystal_I2C.h>
#include <Wire.h>

const int pHPin = A0; // pH 센서 연결 핀

void setup() {
  Serial.begin(9600);
}

void loop() {
  // pH 값을 측정
  float pHValue = analogRead(pHPin);

  // pH 값을 전압 값으로 변환
  pHValue = (pHValue / 1024) * 5.0;

  // pH 값을 실제 pH 값으로 변환
  pHValue = 7 - (pHValue - 2.5) / 0.18;

  // 측정된 pH 값을 시리얼 모니터에 출력
  Serial.print("pH Value: ");
  Serial.println(pHValue);

  // 여기에 수질 관리에 필요한 추가 로직을 구현할 수 있습니다.
  
  delay(1000); // 1초 간격으로 측정
}
