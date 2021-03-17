from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
import time


def main():
    Scheduler.Scheduler.getInstance()
    for i in range(0,100):
        Scheduler.Scheduler.getInstance().run()
        print("Hello")
        time.sleep(0.1)
main()
print("Hello")
    