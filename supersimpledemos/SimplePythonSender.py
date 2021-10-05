#!/usr/bin/env python3
import serial
import time

data = [90.12,90.12,90.12,90.12,90.12,90.12,90.12,90.12,1] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable

ser = serial.Serial('/dev/ttyACM0', 1000000, timeout=1)
dataIn = ser.readline().decode('utf-8').rstrip()
while dataIn != 'A':
    ser.write("A".encode('utf-8'))
    time.sleep(0.001)
    dataIn = ser.readline().decode('utf-8').rstrip()
    print(dataIn)


while True:

    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]}".encode('utf-8'))
    time.sleep(0.2)
