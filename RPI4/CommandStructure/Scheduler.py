from Subsystem import Subsystem
from Command import Command

class Scheduler:
    _instance = None
    def __init__(self):
        self.dictionnary = dict()
        self.triggers = []
        self.scheduledCommands = []
    def getInstance():
        if self._instance is None:
            self._instance = Scheduler()
        return self.instance

    def addSubsystem(self, subsystem):
        self.dictionnary.update({subsystem:None})
    def scheduleCommand(self, command):
        self.scheduledCommands.append(command)
    def addTrigger(self,trigger):
        self.triggers.append(trigger)
    def run(self):
        """
            1- update Sub.periodic()
            2- schedule trigger
            3- associate Command to sub
            4- run commands
        """
        for i in self.dictionnary:
            i.periodic()
        for i in self.triggers:
            if i.get():
                self.scheduleCommand(i.getCommand())
        for i in self.scheduledCommand:
            if :
    #def

Command.Command()

print ("hlelo")