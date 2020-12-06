//포트 지정
int sw1 = 12;
int led1 = 10;
int sw2 =5;
int led2=3;

void setup(){
  pinMode(led1,OUTPUT); //출력
  pinMode(led2,OUTPUT);
  pinMode(sw1,INPUT_PULLUP); //입력 pullup은 floating현상 방지
  pinMode(sw2,INPUT_PULLUP);
  
}
void loop(){
  if(digitalRead(sw1) ==LOW) //스위치 값 가져옴. 눌리면
    digitalWrite(led1,HIGH); //led on
  else
    digitalWrite(led1,LOW); //스위치 닫히면 off

  if(digitalRead(sw2) ==LOW)
    digitalWrite(led2,HIGH);
  else
    digitalWrite(led2,LOW);

    
}
