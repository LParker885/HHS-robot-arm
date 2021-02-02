import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
arduino.flush()
joints = [90,90,90,90,90]
fast = 0
moveEnabled = 1

for j in range(0,4):
  for i in range(0,180):      #cycle through the joint positions to sweep them back and forth
    joints[j] = i
    arduino.write(f"a{joints[0]}a{joints[1]}a{joints[2]}a{joints[3]}a{joints[4]}a{moveEnabled}a{fast}a".encode('utf-8'))  #this line is the important one, it actually sends the data to the arduino
    while ack != "A":                                            #don't overload the arduino, wait untill it has sent the ack character to continue
      ack = arduino.readline().decode('utf-8').rstrip()
    time.sleep(0.1)
  for i in range(180,90):      #cycle through the joint positions to sweep them back and forth
    joints[j] = i
    arduino.write(f"a{joints[0]}a{joints[1]}a{joints[2]}a{joints[3]}a{joints[4]}a{moveEnabled}a{fast}a".encode('utf-8'))  #this line is the important one, it actually sends the data to the arduino
    while ack != "A":                                            #don't overload the arduino, wait untill it has sent the ack character to continue
      ack = arduino.readline().decode('utf-8').rstrip()
    time.sleep(0.1)
moveEnabled = 0