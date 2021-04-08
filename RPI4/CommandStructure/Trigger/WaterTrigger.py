from . import Trigger
import time

class WaterTrigger(Trigger.Trigger):
    minLevel = 730
    minDelayBetweenTriggers = 15   #En secondes, pour tester
    def __init__(self, subsystem, command):
        super().__init__(command)
        self.command = command
        self.waterLevel = subsystem
        self.startTime = 0      #En secondes
        
    def get(self):
        self.cond = (self.waterLevel.getLevel() < WaterTrigger.minLevel) and (time.time() - self.startTime >= WaterTrigger.minDelayBetweenTriggers)
        
        if self.cond:
            self.startTime = time.time()
        return self.cond
