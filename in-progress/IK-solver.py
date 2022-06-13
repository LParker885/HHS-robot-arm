import math
from tkinter import Y
jls = [12,24,18,8]

def solveIK(x,y,z,hand_angle):
    angs = [90,90,90,90]
    #X is straight out, Y is up, Z is to the right, hand angle is the requested angle for the wrist from horizontal
    #ignoring the hand for now
    
    angs[0] = 360*((math.atan(z/x))/(2*math.pi))

    r=math.sqrt((x**2)+(z**2))
    y=y-(jls[3]*math.sin(hand_angle))
    x=x-(jls[3]*math.cos(hand_angle))

    d=math.sqrt(((y-jls[0])**2)+(r**2))
    
    print((jls[1]**2)+(d**2)-(jls[2]**2)/(2*jls[1]*d))
    print((y-jls[0])/r)
    angs[1] = 360*((math.acos((jls[1]**2)+(d**2)-(jls[2]**2)/(2*jls[1]*d))+math.atan((y-jls[0])/r))/(2*math.pi))
    angs[2] = 360*(((math.pi/2)+((math.pi)-math.acos((jls[1]**2)+(jls[2]**2)-(d**2)/(2*jls[1]*jls[2]))))/(2*math.pi))
    
    angs[3] = (180-angs[1]-(angs[2]-90))+hand_angle



    return angs

while 1:
    x=float(input())
    y=float(input())
    z=float(input())
    h=float(input())
    print(solveIK(x,y,z,h))
