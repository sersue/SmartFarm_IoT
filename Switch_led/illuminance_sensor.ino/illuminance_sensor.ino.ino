
int CDS = A1;
int LED = 5;

void setup(){
  Serial.begin(9600);
  pinMode(CDS,INPUT);
  pinMode(LED,OUTPUT);
}

void loop(){
  CDS = analogRead(A1);
  Serial.print("CDS_Sensor:");
  Serial.println(CDS);

  if(CDS>200){
    digitalWrite(LED,HIGH);
    Serial.println("LED ON");
  }
  else{
    digitalWrite(LED,LOW);
    Serial.println("LED OFF");
    
  }
  delay(1000);
}
