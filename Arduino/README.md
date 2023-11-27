### AutoFeeding

    if(digitalRead(LittlePin) == HIGH){ //버튼이 눌렸는지 확인
      Pos = 30; //서보모터 각도 지정
      myservo.write(Pos); //서보모터 제어
      delay(1000); 
      Pos = 0; //서보모터 각도 초기값으로 지정 
      myservo.write(Pos);
    }

핀이 HIGH 인지 LOW 인지 판단하여 서보모터를 제어


### Waterdetection

     if(val >= 500){
        Serial.println("물 넘침 위험");
        delay(5000);
      }
      else if(val <= 100) {
        Serial.println("물 부족 위험");
        delay(5000);
      }

수위를 감지해 기준을 넘거나 모자랄시 경고 발생


### Watermeasurement


      // 아날로그 값을 전압으로 변환
      voltage = (rawValue / 1024.0) * 5.0;

      // 전압을 pH 값으로 변환 (이 부분은 pH 센서의 특정 데이터시트에 따라 달라질 수 있음)
      pHValue = pHValue = 7 - (voltage - VOffset); 

      // 결과를 시리얼 모니터에 출력
      Serial.print("Raw Value: ");
      Serial.print(rawValue);
      Serial.print("\tVoltage: ");
      Serial.print(voltage);
      Serial.print("\tpH Value: ");
      Serial.println(pHValue);

전압을 PH 값으로 변환하여 시리얼 모니터에 출력


### AutomaticDoor

    if(distance < 15){ //거리가 15cm 미만일떄
        myservo.attach(ServoPin);
        Pos = 90;
        myservo.write(Pos); // 서보모터 제어
        delay(1000);
        myservo.detach();
      }
      else{
        myservo.attach(ServoPin);
        Pos = 0;
        myservo.write(Pos);
        delay(1000);
        myservo.detach();
      }

초음파를 이용해 일정 거리 미만일 때 자동으로 문이 열림


###
