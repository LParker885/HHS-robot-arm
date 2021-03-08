#include <PID_v1.h>  //PID loop from http://playground.arduino.cc/Code/PIDLibrary
#include <Servo.h>

//PID tuning variables (in arrays of course for iteration)
const double Pk[] = {0.5, 0.5, 0.5, 0.5, 0.5};
const double Ik[] = {0, 0, 0, 0, 0};
const double Dk[] = {0, 0, 0, 0, 0};

const double Pkf[] = {2, 2, 2, 2, 2};
const double Ikf[] = {0.01, 0.01, 0.01, 0.01, 0.01};
const double Dkf[] = {0.02, 0.02, 0.02, 0.02, 0.02};

//PID input/output variable arrays
double Setpoint[5];
double Input[5];
double Output[5];

//PID objects to control the main motors
PID PID1(&Input[0], &Output[0], &Setpoint[0], Pk[0], Ik[0], Dk[0], DIRECT);
PID PID2(&Input[1], &Output[1], &Setpoint[1], Pk[1], Ik[1], Dk[1], DIRECT);
PID PID3(&Input[2], &Output[2], &Setpoint[2], Pk[2], Ik[2], Dk[2], DIRECT);
PID PID4(&Input[3], &Output[3], &Setpoint[3], Pk[3], Ik[3], Dk[3], DIRECT);
PID PID5(&Input[4], &Output[4], &Setpoint[4], Pk[4], Ik[4], Dk[4], DIRECT);
PID *PidP[] = {&PID1, &PID2, &PID3, &PID4, &PID5}; //pointer array to allowe each of these to be iterated through in a for loop

//servo objects for the servo channels going to the end effector
Servo hand1;
Servo hand2;
Servo hand3;
Servo *servoP[] = {&hand1, &hand2, &hand3}; //pointer array to allow each of these to be iterated through in a for loop

//array to hold analog readings
int pot[] = {0, 0, 0, 0, 0};


//serial input and positioning variables
float pos[] = {90, 90, 90, 90, 90, 90, 90, 90, 0, 0}; // joint1, joint2, joint3, joint4, joint5, hand1, hand2, hand3, enable move, fast mode


//arrays for pin values
const byte pinPOT[] = {A0, A1, A2, A3, A4}; //analog inputs that the feedback potentiometers are attached to
const byte pinPWM[] = {3, 5, 6, 9, 11}; //PWM pins that the speed channel of motor control are attached to
const byte pinDIR[] = {2, 4, 7, 8, 10}; //non-PWM pins that the direction channel of motor control are attached to
const byte pinHAND[] = {14, 15, 16}; //pins the hand servo channels are attached to
const byte pinEstop = 17;

void setup() {
  pinMode(pinEstop,OUTPUT);
  
  for (byte i = 0; i < 5; i++) { //iterate through the PID controllers to set them up
    pinMode(pinPOT[i], INPUT); //set the pins for each motor controller and feedback pot to inputs/outputs
    pinMode(pinPWM[i], OUTPUT);
    pinMode(pinDIR[i], OUTPUT);
    PidP[i]->SetMode(AUTOMATIC);
    PidP[i]->SetOutputLimits(-255, 255); //set the output limits to -255 to 255 for arduino's analogWrite, with a negative for direction
    PidP[i]->SetSampleTime(20);

  }

  for (byte i = 0; i < 3; i++) { //iterate through the servo objects to attach them to their proper pins
    servoP[i]->attach(pinHAND[i]);
  }

  Serial.begin(115200); //start up the serial communication through the onboard USB port to talk to the Raspberry Pi or whatever else
}



void loop() {

  while (pos[8] == 1) { //check that the motor-enable value has been set to 1, it's default is 0.
    digitalWrite(pinEstop,HIGH);
     for (byte i = 0; i < 5; i++) {   //iterate through each joint
  
       if (pos[9] == 1) {
         PidP[i]->SetTunings(Pkf[i], Ikf[i], Dkf[i]);
       } else {
         PidP[i]->SetTunings(Pk[i], Ik[i], Dk[i]);
       }
       
       pot[i] = analogRead(pinPOT[i]);               //get the inputs for the PID controller and run Compute() to put the output in Output[]
       
       Setpoint[i] = map(pos[i], 0, 180, -255, 255);
       Input[i] = map(pot[i], 0, 1023, -255, 255);
        PidP[i]->Compute(); // uses the -> operater instead of the . operater because PidP is a pointer, not the actual object
        
        if (Output[i] > 0) {                    //these if statements account for forward and reverse without a second variable
          analogWrite(pinPWM[i], Output[i]);
         digitalWrite(pinDIR[i], LOW);
       }
       else if (Output[i] < 0) {
         if(i != 0 && i != 1){
          analogWrite(pinPWM[i], 255 - (abs(Output[i])));   //flip-flop the pwm signal, because the direction is now HIGH and the difference should still be the same
         digitalWrite(pinDIR[i], HIGH);
         } else{
           analogWrite(pinPWM[i], abs(Output[i])); //because the turret motor is run off of a different motor driver chip that does not need flippy-floppy PWM
           digitalWrite(pinDIR[i], HIGH);
         }
      }
    }
    for (byte i = 5; i < 8; i++) {  //iterate through the servo objects and set them to the specified positions
      servoP[i - 5]->write(pos[i]); // uses the -> operater instead of the . operater because servoP is a pointer, not the actual object
    }
    
  }
    digitalWrite(pinEstop,LOW);
}



//handler for serial input
void serialEvent() {
  if (Serial.available()) {  //makes sure that all the data is read if multiple sends happen
    for (int i = 0; i < 10; i++) {
      pos[i] = Serial.parseFloat();  //data coming in loks like this: "a90.3a180.5a49.7 etc.", with the charactors being neccesary for clean separation
    }
    Serial.println("A");
  }
}
