
import serial
import time






data = [90,90,90,90,90,90,90,90,0,0,180] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast,res
#                                          0 1  2  3  4  5  6  7  8            9   10
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
dataIn = ser.readline().decode('utf-8').rstrip()
while dataIn != 'A':
    ser.write("A".encode('utf-8'))
    time.sleep(0.001)
    dataIn = ser.readline().decode('utf-8').rstrip()
    print(dataIn)


def changeVals(whichone,val):
   data[whichone]=val

def getInput(data):
    print(data)
    temp=data.split(',')
    pos = temp[0]
    val = temp[1]
    if pos == 1:
        val = (180-((val+40)/(180+40))*180)
    changeVals(int(pos),float(val))



while 1:
    getInput(input())
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]},{data[10]}".encode('utf-8'))
    time.sleep(0.4)