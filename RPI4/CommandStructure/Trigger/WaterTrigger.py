from . import Trigger
import time

class WaterTrigger(Trigger.Trigger):
    minLevel = 225 # To Change #In cm
    minDelayBetweenTriggers = 60   #To Change #In seconds 
    def __init__(self, subsystem, command):
        super().__init__(command)
        self.command = command
        self.waterLevel = subsystem
        #When the program first boots up, wait 5 seconds before executing anything
        self.startTime = time.time()- WaterTrigger.minDelayBetweenTriggers + 5      
        
    def get(self):
        self.cond = (self.waterLevel.getLevel() < WaterTrigger.minLevel) and (time.time() - self.startTime >= WaterTrigger.minDelayBetweenTriggers)
        if self.cond:
            self.startTime = time.time()
        print("tried")
        return self.cond
