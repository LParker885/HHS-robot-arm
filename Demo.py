#############################################################
#This demo program shows how the custom library could be utilized in order to pick up and rearrange small blocks at different positions
#
#############################################################

from RobotArm import Robotarm
import time

arm = Robotarm.Robot()

posarray = [
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 1
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 2
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 3
                [[90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110], [90,90,90,90,90,110]]  # 4

                
]

def pickupnputdown(frompos, topos):
    arm.interpolate(posarray[frompos][0],20,3)
    time.sleep(0.5)
    arm.interpolate(posarray[frompos][1],30,5)
    time.sleep(0.25)
    arm.interpolate(posarray[frompos][2],20,3)
    time.sleep(0.25)
    arm.interpolate(posarray[frompos][3],15,2)
    time.sleep(0.5)
    
    arm.interpolate(posarray[topos][3],15,2)
    time.sleep(0.5)
    arm.interpolate(posarray[topos][2],30,5)
    time.sleep(0.25)
    arm.interpolate(posarray[topos][1],20,3)
    time.sleep(0.25)
    arm.interpolate(posarray[topos][0],30,5)
    time.sleep(0.5)
    return





while 1:
    arm.go()
    pickupnputdown(3,2)
    pickupnputdown(4,1)
    pickupnputdown(1,3)
    pickupnputdown(2,4)
    arm.interpolate([90,90,90,90,90,110],35,2)
    arm.stop()
    time.sleep(2)

