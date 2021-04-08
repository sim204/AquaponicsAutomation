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
import RPi.GPIO as GPIO


def main():
    Deserialise.Deserialise.getInstance().update()
    WaterSubsystem = WaterLevel.WaterLevel()
    WaterCommand = AdjustWaterLevel.AdjustWaterLevel(WaterSubsystem)
    WaterTrig = WaterTrigger.WaterTrigger(WaterSubsystem,WaterCommand)
    Scheduler.Scheduler.getInstance().addSubsystem(WaterSubsystem)
    Scheduler.Scheduler.getInstance().addTrigger(WaterTrig)
    previousTime = time.time()
    
    while True:
        Deserialise.Deserialise.getInstance().update()
        Scheduler.Scheduler.getInstance().run()
        time.sleep(0.1)
try:
    main()
finally:
    GPIO.cleanup()