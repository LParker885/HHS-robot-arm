import thread
import network
import serial
import time

data = [90,90,90,90,90,90,90,90,0,0,360] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast,resolution

stillConnected = 1

baseHeight = 24
baseRadius = 9
joint1Length = 24
joint2Length = 24
handLength = 9




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
    r = temp[0]
    x = temp[1]
    y = temp[2]
    ha1 = temp[3]
    ha2 = temp[4]
    
    #joint1 = r
    #joint3 = (cos⁻¹((joint1length²+joint2length²)-(sqrt(x²+y²))/(2*joint2length*joint1length))/2 (/2 for 360 res cuz 0-360=0-180)
    #joint2 = ((cos⁻¹((joint1length²+sqrt(x²+y²))-(joint2length²)/(2*joint2length*joint1length))+(cos⁻¹(y/x)))/2 (/2 for 360 res, cuz 0-360=0-180)
    
    #data[0] = joint1
    #data[1] = joint2
    #data[2] = joint3
    data[3] = ha1
    data[4] = ha2

network.wait(whenHearCall=getNet)

def doSend():
  while network.isConnected():
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},{data[10]},".encode('utf-8'))
    time.sleep(0.1)

thread.start_new_thread(doSend,(,))    

while True:
  pass
    
    
    
    
    
    
    
    
    
