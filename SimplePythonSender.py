#!/usr/bin/env python3
import serial
import time

data = [90,90,90,90,90,90,90,90,1,0] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()

def changeVals(whichone,val):
    data[whichone] = val

def sendToArduino():
    ser.write(f"a{data[0]}a{data[1]}a{data[2]}a{data[3]}a{data[4]}a{data[5]}a{data[6]}a{data[7]}a{data[8]}a{data[9]}a".encode('utf-8'))
    
while True:
    sendToArduino()
    time.sleep(3)
