from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
from CommandStructure.Subsystem import WaterLevel
from CommandStructure.Subsystem import LightLevel
from CommandStructure.Command import AdjustWaterLevel
from CommandStructure.Command import SendToDatabase
from CommandStructure.Trigger import WaterTrigger
from LowLevel import Deserialise
from LowLevel import MotorController
from LowLevel import AnalogRead
import time
import RPi.GPIO as GPIO


def main():
    Deserialise.Deserialise.getInstance().update()
    
    WaterSubsystem = WaterLevel.WaterLevel()
    LightSubsystem = LightLevel.LightLevel()
    
    
    DBCommand = SendToDatabase.SendToDatabase(WaterSubsystem,LightSubsystem)
    WaterCommand = AdjustWaterLevel.AdjustWaterLevel(WaterSubsystem)
    
    WaterTrig = WaterTrigger.WaterTrigger(WaterSubsystem,WaterCommand)
    
    Scheduler.Scheduler.getInstance().addSubsystem(WaterSubsystem)
    Scheduler.Scheduler.getInstance().addSubsystem(LightSubsystem)
    Scheduler.Scheduler.getInstance().addTrigger(WaterTrig)
    Scheduler.Scheduler.getInstance().scheduleCommand(DBCommand)
    previousTime = time.time()
    while True:
        Deserialise.Deserialise.getInstance().update()
        Scheduler.Scheduler.getInstance().run()
        time.sleep(0.1)
try:
    main()
finally:
    GPIO.cleanup()