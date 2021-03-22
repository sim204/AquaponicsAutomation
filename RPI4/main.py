from CommandStructure import Scheduler
from CommandStructure import Command
from CommandStructure import Subsystem
import time


def main():
    while True:
        #print(str(i) + ": ")
        Scheduler.Scheduler.getInstance().run()
        time.sleep(0.1)
main()
    