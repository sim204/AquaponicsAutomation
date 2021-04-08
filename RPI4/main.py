from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
from CommandStructure.Subsystem import WaterLevel
from CommandStructure.Command import AdjustWaterLevel
from CommandStructure.Trigger import WaterTrigger
from LowLevel import Deserialise
from LowLevel import MotorController
from LowLevel import AnalogRead
import time


def main():
    WaterSubsystem = WaterLevel.WaterLevel()
    WaterCommand = AdjustWaterLevel.AdjustWaterLevel(WaterSubsystem)
    WaterTrig = WaterTrigger.WaterTrigger(WaterSubsystem,WaterCommand)
    Scheduler.Scheduler.getInstance().addSubsystem(WaterSubsystem)
    Scheduler.Scheduler.getInstance().addTrigger(WaterTrig)
    
    previousTime = time.time()
    i = 0
    while time.time() - previousTime < 60:
        Deserialise.Deserialise.getInstance().update()
        Scheduler.Scheduler.getInstance().run()
        if i%10 == 0:
            print("WaterLevel: ", WaterSubsystem.getLevel())
            print("time: ", time.time()-previousTime)
        i = i + 1
        time.sleep(0.1)
        
main()
    