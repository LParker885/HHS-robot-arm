const byte pinPOT[] = {A0, A1, A2, A3, A4}; //analog inputs that the feedback potentiometers are attached to
const byte pinPWM[] = {3, 5, 6, 9, 11}; //PWM pins that the speed channel of motor control are attached to
const byte pinDIR[] = {2, 4, 7, 8, 10}; //non-PWM pins that the direction channel of motor control are attached to
const byte pinHAND[] = {14, 15, 16}; //pins the hand servo channels are attached to
const byte pinEstop = 17;

void setup(){
  for (byte i = 0; i < 5; i++) { //iterate through the PID controllers to set them up
    pinMode(pinPOT[i], INPUT); //set the pins for each motor controller and feedback pot to inputs/outputs
    pinMode(pinPWM[i], OUTPUT);
    pinMode(pinDIR[i], OUTPUT);
 
  }
}
void loop(){
  for(int i = 0; i <= 4; i++){
    for(int j = 0, j<=255; j++){
analogWrite(pinPWM[i], j);
digitalWrite(pinDIR[i], LOW);
      delay(10);
    }
    for(int j = 255, j<=0; j--){
analogWrite(pinPWM[i], j);
digitalWrite(pinDIR[i], LOW);
      delay(10);
    }
  }
}
