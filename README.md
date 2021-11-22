# ---- Note -----
Readme is in progress, as is the rest of the repository, and so might not be updated with the latest about where code is and what folders are.
Being thusly warned, here is the somewhat current readme, which should be taken more as guidelines than a Pirate's Code of Honor. 




# Robot arm!
This code is for the robot arm at HHS. 
It has a few folders: maintenence, supersimpledemos, and networked-demos. 

Maintenence should not worried about unless the robot needs retuning or a reflash of the firmware, but feel free to look if you are interested. 

supersimpledemos has simple demos that are run on the pi inside the robot arm. 

networked-demos has three folders: 
- a folder for basic networking stuff, that has the dependancy (network.py) and a basic python network chat app
- a folder for recieve side stuff, which are the python programs that run on the pi inside the robot arm, and are basically just middlemen (sometimes with a bit of calculation for taking one kind of input and feeding it to the arduino like the arduino likes)
- a folder for send side stuff, which are the python programs that run on the pi outside of the robot arm that is connected with an ethernet cable, and send data, commands, input, whatever you want to call it, for super easy interaction. 
