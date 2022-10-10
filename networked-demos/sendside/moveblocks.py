#sweep test!
import network
import math
import time
ip = "169.254.126.87"

network.call(ip)
jointdata = [90,90,90,90,90,110]
 #           0   1  2  3  4  5
def sayNet():
    for i in range(0,6):
        network.say("{0},{1}".format(i,jointdata[i]))
        print("{0},{1}".format(i,jointdata[i]))

def interpolate(newData,steps,timego):
    increment = [0,0,0,0,0,0]

    for pos in range(0,6):
        temp = newData[pos]-jointdata[pos]
        increment[pos] = round(temp/steps,2)
    print("increment",increment)
    for t in range(0,steps):
        for pos in range(0,6):
            jointdata[pos] = round(jointdata[pos] + increment[pos],2)
        sayNet()

        time.sleep(timego/steps)
    for pos in range(0,6):
        jointdata[pos] = newData[pos]
    sayNet()

positionArray = [

[128, 112, 13, 77, 88, 134], #over
[128, 112, 13, 88, 88, 134], #down
[128, 112, 13, 88, 88, 102], #pickup on 1
[128, 96, 13, 88, 88, 102], #up
[119, 93, 13, 88, 88, 98], #over
[119, 108, 10, 88, 88, 98], #down
[119, 108, 10, 88, 88, 127], #letgo on 2
[119, 97, 10, 88, 88, 127], #up
[125, 116, 24, 88, 88, 127], #over
[125, 121, 24, 88, 88, 127], #down
[125, 121, 24, 88, 88, 99], #pickup on 3
[125, 114, 24, 88, 88, 99], #up
[128, 100, 9, 88, 88, 99], #over
[128, 112, 13, 88, 88, 99], #down
[128, 112, 13, 88, 88, 115], #letgo on 1
[128, 102, 11, 88, 88, 115], #up
[119, 102, 11, 88, 88, 115], #over
[119, 108, 10, 88, 88, 115], #down
[119, 108, 10, 88, 88, 102], #pickup on 2
[119, 104, 11, 88, 88, 102], #up
[125, 113, 23, 88, 88, 100], #over
[125, 121, 24, 88, 83, 100], #down
[125, 121, 24, 88, 83, 126], #letgo on 3
[125, 104, 25, 94, 83, 126] #up
]

while network.isConnected():
    network.say("8,1")
    for i in range(0,24):
        interpolate(positionArray[i],20,3)
        time.sleep(1)