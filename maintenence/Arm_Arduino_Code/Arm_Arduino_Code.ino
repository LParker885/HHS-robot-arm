

#include <PID_v1.h>  //PID loop from http://playground.arduino.cc/Code/PIDLibrary
#include <Servo.h>
#include "Smuuthed.h"

  

//sensor smoothing objects
Smoothed <float> sm1; 
Smoothed <float> sm2;
Smoothed <float> sm3; 
Smoothed <float> sm4;
Smoothed <float> sm5;
Smoothed <float> *smP[] ={&sm1,&sm2,&sm3,&sm4,&sm5};

//PID tuning variables (in arrays of course for iteration)
/*
double Pk[] = {15, 15, 15 , 0,2};
double Ik[] = {2.5, 2,  3,   0,   0};
double Dk[] =- {.5,0.5, 0.5,  0,  0};
*/
double Pk[] = {10, 5, 15 , 10,7};
double Ik[] = {0.5, 0,  0,   4,   0.5};
double Dk[] = {0.2,0.0, 0.1,  0,  0.5};

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

//array to hold analog readings
int pot[] = {0, 0, 0, 0, 0};


//serial input and positioning variables
float pos[] = {90, 90, 90, 90, 90, 90, 90, 90, 0, 0, 180}; // joint1, joint2, joint3, joint4, joint5, hand1, hand2, hand3, enable move, fast mode, input range
byte timeout = 0;


//arrays for pin values
const byte pinPOT[] = {A0, A1, A2, A3, A4}; //analog inputs that the feedback potentiometers are attached to
const byte pinPWM[] = {5, 6, 9, 10, 11}; //PWM pins that the speed channel of motor control are attached to
const byte pinDIR[] = {4, 7, 8, 12, 16}; //non-PWM pins that the direction channel of motor control are attached to
const byte pinHAND[] = {2, 3, 15}; //pins the hand servo channels are attached to
const byte pinEstop = 17;


const int top[] = {980,990,490,960,1000};
const int bottom[] = {70,500,30,120,380};
const int angMin[] = {0,0, 0,  0, 0};
const int angMax[] = {180,180,180,180,180};


void setup() {
  pinMode(pinEstop, OUTPUT);

  for(int motorNumber = 0; motorNumber < 5; motorNumber++){
    pinMode(pinPOT[motorNumber], INPUT); //set the pins for each motor controller and feedback pot to inputs/outputs
    pinMode(pinPWM[motorNumber], OUTPUT);
    pinMode(pinDIR[motorNumber], OUTPUT);
    PidP[motorNumber]->SetMode(AUTOMATIC);
    PidP[motorNumber]->SetOutputLimits(-255, 255); //set the output limits to -255 to 255 for arduino's analogWrite, with a negative for direction
    PidP[motorNumber]->SetSampleTime(20);
    smP[motorNumber]->begin(SMOOTHED_AVERAGE, 30);
  }

hand1.attach(pinHAND[2]);
  for (byte i = 0; i < 2; i++) {
      analogWrite(pinPWM[i], 255);
      digitalWrite(pinDIR[i], LOW);
      
    }
    for (byte i = 2; i < 5; i++) {
      analogWrite(pinPWM[i], 0);
      digitalWrite(pinDIR[i], LOW);
      
    }

  Serial.begin(9600); //start up the serial communication through the onboard USB port to talk to the Raspberry Pi or whatever else
  while (!Serial.available()) {

    delay(10);
  }
  Serial.println('A');

}



void loop() {
  getSerial();
  if (pos[8] == 1 &&  analogRead(pinPOT[1]) != 0 ) { //check that the motor-enable value has been set to 1, it's default is 0.

   // digitalWrite(pinEstop, HIGH);

for(int motorNumber = 0; motorNumber <5; motorNumber++){

      pot[motorNumber] = analogRead(pinPOT[motorNumber]);               //get the inputs for the PID controller and run Compute() to put the output in Output[]
       
      
      Setpoint[motorNumber] = map(max(angMin[motorNumber],min(pos[motorNumber],angMax[motorNumber])), angMin[motorNumber], angMax[motorNumber], -255, 255);
      
      smP[motorNumber]->add(map(pot[motorNumber], bottom[motorNumber], top[motorNumber], -255, 255));
      Input[motorNumber] = smP[motorNumber]->get();
      PidP[motorNumber]->Compute(); // uses the -> operater instead of the . operater because PidP is a pointer, not the actual object



     
       
      if (Output[motorNumber] > 0) {                    //these if statements account for forward and reverse without a second variable
       
       if (motorNumber == 0 || motorNumber == 1 ) {
         
          analogWrite(pinPWM[motorNumber], 255 - abs(Output[motorNumber]));   //flip-flop the pwm signal, because the direction is now HIGH and the difference should still be the same
          digitalWrite(pinDIR[motorNumber], HIGH);
  
        } else {
          analogWrite(pinPWM[motorNumber], abs(Output[motorNumber])); 
          digitalWrite(pinDIR[motorNumber], HIGH);
        }
     
       
      }
      else if (Output[motorNumber] <= 0) {
        if (motorNumber == 0 || motorNumber == 1 ) {
          analogWrite(pinPWM[motorNumber], 255 - (abs(Output[motorNumber])));   
          digitalWrite(pinDIR[motorNumber], LOW);
        } else {
          analogWrite(pinPWM[motorNumber], abs(Output[motorNumber]));
          digitalWrite(pinDIR[motorNumber], LOW);
        }
      }

    
 
     
      hand1.write(pos[5]); 
  
  
  
}
  }
  else if (pos[8] == 0 ||  analogRead(pinPOT[1]) == 0) {
   // digitalWrite(pinEstop, LOW);
   pos[8] = 0;
   for (byte i = 0; i < 2; i++) {
      analogWrite(pinPWM[i], 255);
      digitalWrite(pinDIR[i], LOW);
      
    }
    for (byte i = 2; i < 5; i++) {
      analogWrite(pinPWM[i], 0);
      digitalWrite(pinDIR[i], LOW);
      
    }
 

  }

}



void getSerial() {
  if (Serial.available()) {

    String rxString = "";
    String strArr[11]; //Set the size of the array to equal the number of values you will be receiveing.
    //Keep looping until there is something in the buffer.

    while (Serial.available()) {
      //Delay to allow byte to arrive in input buffer.
      delay(2);
      //Read a single character from the buffer.
      char ch = Serial.read();
      //Append that single character to a string.
      rxString += ch;

    }
    int stringStart = 0;
    int arrayIndex = 0;
    for (int i = 0; i < rxString.length(); i++) {
      //Get character and check if it's our "special" character.
      if (rxString.charAt(i) == ',') {
        //Clear previous values from array.
        strArr[arrayIndex] = "";
        //Save substring into array.
        strArr[arrayIndex] = rxString.substring(stringStart, i);
        //Set new string starting point.
        stringStart = (i + 1);
        char buf[strArr[arrayIndex].length() + 1];
        strArr[arrayIndex].toCharArray(buf, strArr[arrayIndex].length() + 1);
        pos[arrayIndex] = atoi(buf);
        arrayIndex++;
      }
    }
  }

}
