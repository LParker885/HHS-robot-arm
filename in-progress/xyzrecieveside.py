# this is the code that the Raspberry Pi inside of the robot arm would be told to run via SSH. 

#inverse kinematics attempt 1: will most likely just use a library for this. 

import thread
import network
import serial
import time
import math
import tinyik
import numpy as np


data = [90,90,90,90,90,90,90,90,0,0,360] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast,resolution

stillConnected = True

baseHeight = 24
joint1Length = 24
joint2Length = 24
wristlength = 6
handLength = 8


arm = tinyik.Actuator(['y',[baseHeight,.0,.0],'z',[joint1Length, .0, .0], 'z',[joint2Length, .0, .0], 'z', [wristlength,.0,.0],'x',[handLength,.0,.0]])



ser = serial.Serial('/dev/ttyACM0', 1000000, timeout=1)
dataIn = ser.readline().decode('utf-8').rstrip()
while dataIn != 'A':
    ser.write("A".encode('utf-8'))
    time.sleep(0.001)
    dataIn = ser.readline().decode('utf-8').rstrip()
    print(dataIn)


def getNet(data):
    print(data)
    temp=data.split(',')
    x = temp[0]
    y = temp[1]
    z = temp[2]
    data[5] = temp[3] #hand1
    data[6] = temp[4] #hand2
    arm.ee = [x,y,z]
    data[0] = np.rad2deg(arm.angles)[0] #base
    data[1] = np.rad2deg(arm.angles)[1] #shoulder
    data[2] = np.rad2deg(arm.angles)[2] #elbow
    data[3] = np.rad2deg(arm.angles)[3] #wrist
    data[4] = np.rad2deg(arm.angles)[4] #wristspinny


   
   

network.wait(whenHearCall=getNet)

def doSend():
  while network.isConnected():
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},{data[10]}".encode('utf-8'))
    time.sleep(0.1)

thread.start_new_thread(doSend,(,))    

while True:
  pass
    
    
    
    
    
    
    
    
    
