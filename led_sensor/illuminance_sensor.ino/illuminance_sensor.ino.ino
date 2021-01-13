
int CDS = A1;
int LED = 5;

void setup(){
  Serial.begin(9600);
  pinMode(CDS,INPUT);
  pinMode(LED,OUTPUT);
  //excel
  Serial.println("CLEARDATA");
  Serial.println("Label,illuminance");

}

void loop(){
  CDS = analogRead(A1);
  Serial.print("C");
  Serial.println(CDS);

  if(CDS>200){
    digitalWrite(LED,HIGH);
//    Serial.println("ON");
  }
  else{
    digitalWrite(LED,LOW);
//    Serial.println("OFF");
    
  }
  delay(10000);
  Serial.end();

  
  
}
