
// this program is so that the potentiometer values at the limits of motion can be recorded for tuning, with manual motion of the arm. 

void setup() {
Serial.begin(9600);
 
 pinMode(A0,INPUT);
 pinMode(A1,INPUT);
 pinMode(A2,INPUT);
 pinMode(A3,INPUT);  
 pinMode(A4,INPUT);
 
}

void loop(){
 for(int i = 0; i < 6; i++){
  Serial.print(analogRead(i));
  Serial.print("\t");
   
 }
  Serial.println();
  
}
