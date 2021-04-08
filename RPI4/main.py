from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
from LowLevel import Deserialise
from LowLevel import MotorController
from LowLevel import AnalogRead
import time


def main():
    test = MotorController.MotorController(15,18,14)
    test2 = AnalogRead.AnalogRead(0)
        
    while True:
        Deserialise.Deserialise.getInstance().update()
        temp = float(((2*test2.get()-512)/1023) - 0.5)
        test.setPercentage(temp)
        print(temp)
        time.sleep(0.1)
        
main()
    