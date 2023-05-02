#sweep test!
import network
import math
import time
ip = "169.254.126.87"

#positions
#     1                  2
#     3                  4
#                    over, open               down, open         down, closed           over, closed
posarray = [
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 1
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 2
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 3
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 4

                
]


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

def pickupnputdown(frompos, topos):
    interpolate(posarray[frompos][0],20,3)
    time.sleep(0.5)
    interpolate(posarray[frompos][1],30,5)
    time.sleep(0.25)
    interpolate(posarray[frompos][2],20,3)
    time.sleep(0.25)
    interpolate(posarray[frompos][3],15,2)
    time.sleep(0.5)
    
    interpolate(posarray[topos][3],15,2)
    time.sleep(0.5)
    interpolate(posarray[topos][2],30,5)
    time.sleep(0.25)
    interpolate(posarray[topos][1],20,3)
    time.sleep(0.25)
    interpolate(posarray[topos][0],30,5)
    time.sleep(0.5)
    return

while network.isConnected():
    network.say("8,1")
    time.sleep(1)

    pickupnputdown(3,2)
    pickupnputdown(4,1)
    pickupnputdown(1,3)
    pickupnputdown(2,4)
    
    interpolate([90,90,90,90,90,110],35,2)
    time.sleep(0.25)
    network.say("8,0")
    time.sleep(2)