#sweep test!
import network
import time
ip = "169.168.1.101"

network.call(ip)



while network.isConnected():

    network.say("8,1")
    network.say("9,1")
    num = 2
    for val in range(90,180,5):
        out = str(num) + "," + str(val)
        network.say(out)
        time.sleep(0.1)
    for val in range(180,0,-5):
        out = str(num) + "," + str(val)
        network.say(out)
        time.sleep(0.1)
    for val in range(0,95,5):
        out = str(num) + "," + str(val)
        network.say(out)
        time.sleep(0.1)
        
    time.sleep(1)
    network.say("8,0")
    time.sleep(5)
