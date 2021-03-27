
import network


network.call("169.168.1.101")

while network.isConnected():
  
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  
  #send data like this: 
  # 0,9,1   -- OPTIONAL, turns on "fast mode" to tune the ideal optimal PID settings for most agile operation. otherwise, you are tuning the "learning mode" which moves slower to give more time to whack the estop in case of a crash. 
  # 0,9,0   -- only necessary if fast mode has been turned on and you wish to also tune the learning mode. 
  # 0,8,1   -- turns on motion
  # 0,2,60  -- (0-4),(0,180) 0-4 for the 5 different joints, 0-180 to move them to see how they react. running the sweeptest too might help if you feel like doing a bunch of program switching. 
  # 0,8,0   -- turns off motion
  # 0,11,1  -- turns on tuning
  # 1,2,0.1,0.01 -- joint,kP,kI,kD  -- new tunings for PID on the joint, formatted as joint then proportional then integral then derivative. GO SLOW, DON'T MAKE TOO BIG OF CHANGES, OR IT *WILL* CRASH!!!!!!!
  # 0,11,1  -- sends the updated tunings
  #         -- wait a second
  # 0,11,0  -- turn off tuning updating
  # do it all over again untill buttery smooth! 
  # once buttery smooth, record the pid values that you used for each joint, and re-flash the arduino sketch with those values in the right places. 
