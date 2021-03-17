#sweep test!
import network
import time
import sys
ip = "169.168.1.101"

network.call(ip)



while network.isConnected():
    phrase = input() #phrase should look like 60,12,16,90,180 or theta,x,y,h1,h2 where theta is the angle as measured from the back of the robot in degrees (facing forward = 180), x is how far out the hand should be in inches, y is how far up it should be in inches, h1 is hand tilt in degrees 0-180, h2 is hand rotation in degrees 0-360
    print(phrase)
    network.say(phrase)
    
    
