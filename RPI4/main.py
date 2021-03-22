from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure.Command import SchedulerTestCommand
from CommandStructure.Subsystem import SubSchedulerTest
from CommandStructure import Subsystem
import time


def main():
    subInstance1 = SubSchedulerTest.SubSchedulerTest()
    instance1 = SchedulerTestCommand.SchedulerTestCommand()
    instance2 = SchedulerTestCommand.SchedulerTestCommand()
    
    Scheduler.Scheduler.getInstance().addSubsystem(subInstance1)
    Scheduler.Scheduler.getInstance().scheduleCommand(instance1)
    Scheduler.Scheduler.getInstance().addSubsystem(None)
    
    for i in range(0,20):
        #print(str(i) + ": ")
        Scheduler.Scheduler.getInstance().run()
        
        if i == 5:
            Scheduler.Scheduler.getInstance().scheduleCommand(instance1)
        time.sleep(0.01)
main()
print("Hello")
    