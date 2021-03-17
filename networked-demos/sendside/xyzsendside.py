#sweep test!
import network
import time
import sys
ip = "169.168.1.101"

network.call(ip)



while network.isConnected():
    phrase = input() #phrase should look like 60,12,16,90,180 or theta,x,y,h1,h2 where theta is the angle as measured from the back of the robot (facing forward = 180), x is how far out the hand should be, y is how far up it should be, h1 is hand tilt, h2 is hand rotation
    print(phrase)
    network.say(phrase)
    
    
