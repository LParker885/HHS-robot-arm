
import network


network.call("169.168.1.101")

while network.isConnected():
  
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  
  #send data like this: 
  # 8,1   -- turns on motion
  # 2,60  -- (0-4),(0,180) 0-4 for the 5 different joints, 0-180 to move them to see how they react. running the sweeptest too might help if you feel like doing a bunch of program switching. 
  # 8,0   -- turns off motion
  # 13,2    -- 11-15, P-value for that axis (11=0,12=1,13=2 etc.) SEE PROPER PID TUNING GUIDLINES TO ADJUST THESE VALUES OR YOU *WILL* CRASH THE MACHIENE!!!!!!!!!!!!
  # 15,0.01 -- 16-20, I-value for that axis
  # 22,0.02 -- 21-26, D-value for that axis
  # 10,1  -- sends the updated tunings
  #       -- wait maybe 5 seconds, maybe less
  # 10,0  -- turn off tuning updating
  # do it all over again untill buttery smooth! 
  # once buttery smooth, record the pid values that you used for each joint, and re-flash the arduino sketch with those values in the right places. 
