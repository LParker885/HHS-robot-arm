#sweep test!
import network
import time
ip = "169.254.126.87"

network.call(ip)



while network.isConnected():

    network.say("8,1")
    num = 2
    for num in range(0,4):
        network.say("8,1")
        for val in range(90,150,2):
            out = str(num) + "," + str(val)
            network.say(out)
            time.sleep(0.2)
        for val in range(150,30,-2):
            out = str(num) + "," + str(val)
            network.say(out)
            time.sleep(0.2)
        for val in range(30,90,3):
            out = str(num) + "," + str(val)
            network.say(out)
            time.sleep(0.2)
        time.sleep(1)
        network.say("8,0")
        time.sleep(1)