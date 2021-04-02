from . import Trigger
from Subsystem import WaterLevel
import time

class WaterTrigger(Trigger, WaterLevel):
    minLevel = 15
    deltaTemps=30   #En secondes, pour tester
    def __init__(self, command):
        super().__init__()
        self.command = AdjustWaterLevel.AdjustWaterLevel()
        self.waterLevel = WaterLevel.WaterLevel()
        self.startTime = 0      #En secondes
        
    def get(self, value):
        self.cond = (waterLevel.get() < minLevel) and (time.time() - startTime() >= deltaTemps)
        if self.cond:
            startTime = time.time()
        return self.cond
