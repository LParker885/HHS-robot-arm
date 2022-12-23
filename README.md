
# ---- Note -----
Website: https://lparker885.github.io/HHS-robot-arm/

Readme is in progress, as is the rest of the repository, and so might not be updated with the latest about where code is and what folders are.
Being so warned, here is the somewhat current readme, designed to be quickly read by a student in a computer science class so that they can get right on with making the robot arm do whatever they want it to:


# ------- HOW TO INSTALL AND USE! --------------

Goto the tutorials page:   https://lparker885.github.io/HHS-robot-arm/website/tutorials.html

Follow the instructions! :)

# simple demo program:

from RobotArm import Robotarm
arm = Robotarm.Robot()

print(arm)
#should return an array looking like this: "[90,90,90,90,90,90,110]"

arm.go()
#arm should start whirring
arm.interpolate([110,110,90,90,90,110,90],20,3)
#should move the arm and the hand slowly to a new position
arm.stop()
#arm should stop whirring

# more (less simple) API explanation
Robot() creates a new robot object. Upon calling, it will connect to the robot arm via ethernet, so please don't try to set up the robot arm object before connecting the two pis and verifying that the network connected with ifconfig. (type ifconfig in the terminal, the eth0 interface should be connected).
This object will return its joint data array when the __str__ function is called. Sorry. But I'll probably not fix that. 

interpolate(newData,steps,time) is a function that causes the robot to interpolate to a new position. Pass an array for newData, which should have 7 elements in this order: [base,shoulder,elbow,wristPitch,wristRoll,Hand1,Hand2]. Steps is simply the number of steps you wish to move through between the current position and newData. time is how long to spend interpolating. The robot can handle 5 steps per second, so for a maximally smooth interpolation, multiply time by 5 and add 5 for buffer if time is greater than 3. 

go() enables PID loops and motor controller output. 

stop() disables PID loops and motor controller output. 

runArray(array, time) will run through a 2-D array of positions of arbitrary length passed to array. [position,position,position,position,etc.]. the positions should look like the newData passed to interpolate(). time is how long the robot should spend going between each position. 



# ----------ignore this stuff its old -----

# Robot arm!
Website: https://lparker885.github.io/HHS-robot-arm/

This code is for the robot arm at HHS. 
It has a few folders: maintenence, supersimpledemos, and networked-demos. 

Maintenence should not worried about unless the robot needs retuning or a reflash of the firmware, but feel free to look if you are interested. 

supersimpledemos has simple demos that are run on the pi inside the robot arm. 

networked-demos has three folders: 
- a folder for basic networking stuff, that has the dependancy (network.py) and a basic python network chat app
- a folder for recieve side stuff, which are the python programs that run on the pi inside the robot arm, and are basically just middlemen (sometimes with a bit of calculation for taking one kind of input and feeding it to the arduino like the arduino likes)
- a folder for send side stuff, which are the python programs that run on the pi outside of the robot arm that is connected with an ethernet cable, and send data, commands, input, whatever you want to call it, for super easy interaction. 
