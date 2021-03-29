from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
import time


def main():
    if False:
        test = AnalogRead.AnalogRead(0)
        test2 = Deserialise.Deserialise.getInstance()
        test3 = PWMWrite.PWMWrite(17)
        test4 = DigitalRead.DigitalRead(27)
        while True:
            for i in range(0,100,1):
                test3.setDutyCycle(i/100)
                time.sleep(0.01)
            for i in range(100,0,-1):
                test3.setDutyCycle(i/100)
                time.sleep(0.01)
    
    while True:
        #print(str(i) + ": ")
        Scheduler.Scheduler.getInstance().run()
        time.sleep(0.1)
        
main()
    