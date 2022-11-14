import tinyik
import numpy as np
import time


arm = tinyik.Actuator(['y',[.05,.0,.0],'z',[1., .0, .0], 'z',[1., .0, .0], 'z', [.1,.0,.0],'x',[.2,.0,.0]])


while 1:
    try:
        for x in range(0,10,1):
            arm.ee=[x/10,1,1]
            print(arm.ee,np.rad2deg(arm.angles))
            time.sleep(0.5)
        for x in range(10,0,-1):
            arm.ee=[x/10,1,1]
            print(arm.ee,np.rad2deg(arm.angles))
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit()