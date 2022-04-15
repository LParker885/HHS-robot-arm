

int pinp = 11;
int pind = 16;


void setup(){
 pinMode(pinp,OUTPUT);
 pinMode(pind,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  while(!Serial.available()){
  }
  
  Serial.println("LOW, Increasing");
  digitalWrite(pind,LOW);
  for(int i = 0; i<256; i+= 10){
   analogWrite(pinp,i); 
   delay(100);
  }
  Serial.println("LOW, Decreasing");
  for(int i = 255; i>=0; i-= 10){
   analogWrite(pinp,i); 
   delay(100);
  }
  delay(1000);
  Serial.println("HIGH, Increasing");
  digitalWrite(pind,HIGH);
  for(int i = 0; i<256; i+= 10){
   analogWrite(pinp,i); 
   delay(100);
  }
  Serial.println("HIGH, Decreasing");
  for(int i = 255; i>=0; i-= 10){
   analogWrite(pinp,i); 
   delay(100);
  }
  delay(1000);
  
  
  Serial.println("HIGH, 0");
  analogWrite(pinp,0);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 0");
  analogWrite(13,0);
  digitalWrite(pind,LOW);
  delay(1000);
  
  Serial.println("HIGH, 255");
  analogWrite(pinp,255);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 255");
  analogWrite(pinp,255);
  digitalWrite(pind,LOW);
  delay(1000);
  
  
   Serial.println("HIGH, 10");
  analogWrite(pinp,10);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 10");
  analogWrite(pinp,10);
  digitalWrite(pind,LOW);
  delay(1000);
  
  Serial.println("HIGH, 245");
  analogWrite(pinp,245);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 245");
  analogWrite(pinp,245);
  digitalWrite(pind,LOW);
  delay(1000);
  
     Serial.println("HIGH, 1");
  analogWrite(pinp,1);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 1");
  analogWrite(pinp,1);
  digitalWrite(pind,LOW);
  delay(1000);
 
   Serial.println("HIGH, 128");
  analogWrite(pinp,128);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 128");
  analogWrite(pinp,128);
  digitalWrite(pind,LOW);
  delay(1000);
 
  Serial.println("HIGH, 254");
  analogWrite(pinp,254);
  digitalWrite(pind,HIGH);
  delay(1000);
  
  Serial.println("LOW, 254");
  analogWrite(pinp,254);
  digitalWrite(pind,LOW);
  delay(1000);
  
}
