
//M1: 70, 980
//M2:990, 500
//M3:30, 490
//M4:120, 90
//M5:990, 380


void setup() {
Serial.begin(115200);
 
 pinMode(A0,INPUT);
 pinMode(A1,INPUT);
 pinMode(A2,INPUT);
 pinMode(A3,INPUT);  
 pinMode(A4,INPUT);
 
}

void loop(){
 for(int i = 0; i < 5; i++){
  Serial.print(analogRead(i));
  Serial.print("\t");
   
 }
  Serial.println();
  delay(100);
  
}
