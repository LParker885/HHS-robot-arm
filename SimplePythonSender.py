import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
arduino.flush()
joints = [90,90,90,90,90]
handServos = [90,90,90]
fast = 0
moveEnabled = 0

while 1:
  arduino.write(f"a{joints[0]}a{joints[1]}a{joints[2]}a{joints[3]}a{joints[4]}a{handServos[0]}a{handServos[1]}a{handServos[2]}a{moveEnabled}a{fast}a".encode('utf-8'))  #this line is the important one, it actually sends the data to the arduino
  while ack != "A":                                            #don't overload the arduino, wait untill it has sent the ack character to continue
    ack = arduino.readline().decode('utf-8').rstrip()
