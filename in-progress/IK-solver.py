import math
jls = [12,24,18,8]
angs = []
def solveIK(x,y,z):
    #X is straight out, Y is up, Z is to the right
    #ignoring the hand for now
    r=math.sqrt((x**2)+(z**2))
    angs[0] = 360*((math.atan(z/x))/(2*math.pi))
    angs[1] = 360*((math.acos((jls[1]**2)+(r**2)-(jls[2]**2)/(2*jls[1]*r))+math.asin((y-jls[0])/r))/(2*math.pi))
    angs[2] = 360*(((math.pi/2)+((math.pi)-math.acos((jls[1]**2)+(jls[2]**2)-(r**2)/(2*jls[1]*jls[2]))))/(2*math.pi))


    return angs
