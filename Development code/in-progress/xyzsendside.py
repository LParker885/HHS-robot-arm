#this is the code that a student in a computer science class would need to write



import network
import time
import sys
ip = "169.168.1.101"

network.call(ip)



while network.isConnected():
    phrase = input() #phrase should look like 60,12,16,90,180 or x,y,z,h1,h2 
    print(phrase)
    network.say(phrase)
    
    
