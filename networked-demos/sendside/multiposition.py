#sweep test!
import network
import time
ip = "169.254.126.87"

network.call(ip)
jointdata = [90,90,90,90,90,110]
 #           0   1  2  3  4  5
def sayNet(data):
    jointdata = data
    for i in range(0,6):
        network.say("{0},{1}".format(i,jointdata[i]))
        print("{0},{1}".format(i,jointdata[i]))




while network.isConnected():

    network.say("8,1")
    sayNet([125, 116, 21, 95, 90, 131]) #over
    time.sleep(2)
    sayNet([125, 116, 21, 115, 90, 131]) #down
    time.sleep(2)
    sayNet([125, 116, 21, 115, 90, 104]) #grab
    time.sleep(2)
    sayNet([120, 112, 41, 115, 90, 102]) #up
    time.sleep(2)
    sayNet([117, 116, 21, 97, 90, 105]) #over
    time.sleep(2)
    sayNet([117, 116, 14, 98, 90, 105]) #down
    time.sleep(2)
    sayNet([117, 116, 14, 98, 90, 130]) #let go
    time.sleep(2)
    sayNet([117, 116, 14, 40, 90, 130]) #up
    time.sleep(2)
    sayNet([117, 87, 14, 40, 90, 130]) #up
    time.sleep(2)
    sayNet([125, 116, 22, 91, 90, 130]) #over
    time.sleep(2)
