
import network
import serial
import time

data = [90,90,90,90,90,90,90,90,0,0,180,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast,res,tunemode,p1,p2,p3,p4,p5,i1,i2,i3,i4,i5,d1,d2,d3,d4,d5

ser = serial.Serial('/dev/ttyACM0', 500000, timeout=1)
dataIn = ser.readline().decode('utf-8').rstrip()
while dataIn != 'A':
    ser.write("A".encode('utf-8'))
    time.sleep(0.001)
    dataIn = ser.readline().decode('utf-8').rstrip()
    print(dataIn)


def changeVals(whichone,val):
   data[whichone]=val

def getNet(data):
    print(data)
    temp=data.split(',')
    pos = temp[0]
    val = temp[1]
    changeVals(int(pos),float(val))

network.wait(whenHearCall=getNet)

while network.isConnected():
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},{data[10]},{data[11]},{data[12]},{data[13]},{data[14]},{data[15]},{data[16]},{data[17]},{data[18]},{data[19]},{data[20]},{data[21]},{data[22]},{data[23]},{data[24]},{data[25]},{data[26]}".encode('utf-8'))
    time.sleep(0.1)
