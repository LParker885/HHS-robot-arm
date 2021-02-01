import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.flush()
joints = [90,90,90,90,90]
fast = 0
moveEnabled = 0

while 1:
  arduino.write(f"a{joints[0]}a{joints[1]}a{joints[2]}a{joints[3]}a{joints[4]}a{moveEnabled}a{fast}a")
  while ack != "A":
    ack = arduino.readline().decode('utf-8').rstrip()
