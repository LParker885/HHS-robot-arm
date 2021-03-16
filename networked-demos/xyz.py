import thread
import network
import serial
import time

data = [90,90,90,90,90,90,90,90,0] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable

stillConnected = 1

baseHeight = 24
baseRadius = 9
joint1Length = 24
joint2Length = 24
handLength = 9




ser = serial.Serial('/dev/ttyACM0', 500000, timeout=1)
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
    #mathymath: xyz to rthetax-thetaz  tri pyramid from offset,thetax,thetaz,        truer to hyp of tri from two joints, ang from tri to joint3 ang,  
    
    

network.wait(whenHearCall=getNet)

def doSend():
  while network.isConnected():
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},".encode('utf-8'))
    time.sleep(0.1)

thread.start_new_thread(doSend,(,))    

while True:
  pass
    
    
    
    
    
    
    
    
    
