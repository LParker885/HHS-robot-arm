
# ------ Website: https://lparker885.github.io/HHS-robot-arm/ -----



# ------- HOW TO INSTALL AND USE! --------------

Goto the tutorials page on the website, it has the best explaination:   https://lparker885.github.io/HHS-robot-arm/website/tutorials.html

Follow the instructions! :)

# simple demo program:

from RobotArm import Robotarm
import time
arm = Robotarm.Robot()

while 1:
    arm.go()
    arm.interpolate([110,90,90,90,90,90,90],20,3)
    arm.interpolate([90,90,90,90,90,90,90],20,3)
    arm.interpolate([90,110,90,90,90,90,90],20,3)
    arm.interpolate([90,90,90,90,90,90,90],20,3)
    arm.stop()
    time.sleep(2)


# more API explanation
Robot() creates a new robot object. Upon calling, it will connect to the robot arm via ethernet, so please don't try to set up the robot arm object before connecting the two pis and verifying that the network connected with ifconfig. (type ifconfig in the terminal, the eth0 interface should be connected).
This object will return its joint data array when the __str__ function is called, throwing an error due to integer arrays not being strings :/  

interpolate(newData,steps,time) is a function that causes the robot to interpolate to a new position. Pass an array for newData, which should have 7 elements in this order: [base,shoulder,elbow,wristPitch,wristRoll,Hand1,Hand2]. Steps is simply the number of steps you wish to move through between the current position and newData. time is how long to spend interpolating. The robot can handle 5 steps per second, so for a maximally smooth interpolation, multiply time by 5 and add 5 for buffer if time is greater than 3. 

go() enables PID loops and motor controller output, effectivley disabling the software e-stop. 

stop() disables PID loops and motor controller output, effectively enabling a software e-stop state. 

runArray(array, time) will run through a 2-D array of positions of arbitrary length passed to array. [position,position,position,position,etc.]. the positions should look like the newData array passed to interpolate(). time is how long the robot should spend going between each position. 

That is the whole API as it stands now. It's pretty simple and intended as am approachable starting point for students who are new to coding, but feel free to build more complex functions off of it - and if you think something more should really be added, submit a pull request! :)

Happy roboting!