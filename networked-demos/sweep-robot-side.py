
import network
import serial
import time

data = [90,90,90,90,90,90,90,90,0,0] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast

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
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},".encode('utf-8'))
    time.sleep(0.1)

ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{0},{data[9]},".encode('utf-8'))



