### AutoFeeding

    if(digitalRead(LittlePin) == HIGH){ //버튼이 눌렸는지 확인
      Pos = 30; //서보모터 각도 지정
      myservo.write(Pos); //서보모터 제어
      delay(1000); 
      Pos = 0; //서보모터 각도 초기값으로 지정 
      myservo.write(Pos);
    }

핀이 HIGH 인지 LOW 인지 판단하여 서보모터를 제어
