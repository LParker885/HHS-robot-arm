#sweep test!
import network
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
    for pos in range(0,5):
        increment[pos] = (newData[pos] - jointdata[pos])/steps
    print("increment",increment)
    for t in range(0,steps):
        for pos in range(0,5):
            jointdata[pos] += increment[pos]
        sayNet()

        time.sleep(timego/steps)


while network.isConnected():

    network.say("8,1")
    newData = [120,120,90,90,90,110]
    interpolate(newData,30,5)
    time.sleep(3)
    newData = [90,90,90,90,90,90]
    interpolate(newData,30,5)
    time.sleep(3)
    newData = [120,120,90,90,90,90]
    interpolate(newData,30,5)
    time.sleep(3)
    newData = [90,90,90,90,90,110]
    interpolate(newData,30,5)
    time.sleep(3)