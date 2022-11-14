# this is the python script that would be called to run on the raspberry pi inside of the robot arm. It parses the network data that it recieves, and sends the properly formatted data to the arduino via serial. 
import network
import serial
import time

data = [90,90,90,90,90,90,90,90,0,0] #j1,j2,j3,j4,j5,h1,h2,h3,moveEnable,fast

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
dataIn = ser.readline().decode('utf-8').rstrip()
while dataIn != 'A':
    ser.write("A".encode('utf-8'))
    time.sleep(0.001)
    dataIn = ser.readline().decode('utf-8').rstrip()
    print(dataIn)




def interpolate(newData,steps,time):
    increment = [0,0,0,0,0,0]
    for pos in range(0,5):
        increment[pos] = (newData[pos] - data[pos])/steps
    for t in range(0,steps):
        for pos in range(0,5):
            data[pos] += increment[pos]

        ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]}".encode('utf-8'))


        time.sleep(time/steps)
    
    
    

def getNet(data):
    
    print(data)
    temp=data.split(',')
    if temp[0] == 1:
        newData = [90,90,90,90,90,110]
        for i in range(0,5):
            newData[i] = int(temp[i])
        
        steps = int(temp[6])
        time = int(temp[7])
        interpolate(newData,steps,time)
    elif temp[0] == 8:
        data[8] = temp[1]
    

    


    

network.wait(whenHearCall=getNet)

while network.isConnected():
    
    ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{data[9]}".encode('utf-8'))
    time.sleep(0.1)

ser.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{0},{data[9]}".encode('utf-8'))



