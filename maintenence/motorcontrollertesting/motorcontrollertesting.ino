void setup(){
 pinMode(13,OUTPUT);
 pinMode(14,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  
  Serial.println("LOW, Speeding up");
  digitalWrite(14,LOW);
  for(int i = 0; i<256; i+= 10){
   analogWrite(13,i); 
   delay(100);
  }
  Serial.println("LOW, Slowing down");
  for(int i = 255; i>=0; i-= 10){
   analogWrite(13,i); 
   delay(100);
  }
  delay(1000);
  Serial.println("HIGH, Speeding up");
  digitalWrite(14,HIGH);
  for(int i = 0; i<256; i+= 10){
   analogWrite(13,i); 
   delay(100);
  }
  Serial.println("HIGH, Slowing down");
  for(int i = 255; i>=0; i-= 10){
   analogWrite(13,i); 
   delay(100);
  }
  delay(1000);
  
  
  Serial.println("HIGH, 0");
  analogWrite(13,0);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 0");
  analogWrite(13,0);
  digitalWrite(14,LOW);
  delay(1000);
  
  Serial.println("HIGH, 255");
  analogWrite(13,255);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 255");
  analogWrite(13,255);
  digitalWrite(14,LOW);
  delay(1000);
  
  
   Serial.println("HIGH, 10");
  analogWrite(13,10);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 10");
  analogWrite(13,10);
  digitalWrite(14,LOW);
  delay(1000);
  
  Serial.println("HIGH, 245");
  analogWrite(13,245);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 245");
  analogWrite(13,245);
  digitalWrite(14,LOW);
  delay(1000);
  
     Serial.println("HIGH, 1");
  analogWrite(13,1);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 1");
  analogWrite(13,1);
  digitalWrite(14,LOW);
  delay(1000);
  
  Serial.println("HIGH, 254");
  analogWrite(13,254);
  digitalWrite(14,HIGH);
  delay(1000);
  
  Serial.println("LOW, 254");
  analogWrite(13,254);
  digitalWrite(14,LOW);
  delay(1000);
  
}
