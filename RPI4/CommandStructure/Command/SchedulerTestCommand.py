from . import Command

class SchedulerTestCommand(Command.Command):
    count = 0
    def __init__(self, subsystem = [None]):
        super().__init__()
        SchedulerTestCommand.count = SchedulerTestCommand.count + 1 
        self._localcount = SchedulerTestCommand.count
        for i in subsystem:
            self.addSubsystem(i)
        
        
    def initialise(self):
        self._iterator = -10
        print("Instance #" + str(self._localcount ))
    def execute(self):
        self._iterator = self._iterator + 1
        print("test: " + str(self._iterator))
    def isFinish(self):
        return self._iterator ==0
    def end(self,isInterrupt):
        print("Test End, Interrupt: " + str(isInterrupt) + "; Instance #" + str(self._localcount ))
    def addSubsystem(self,subsystem):
        self.subsystemList.append(subsystem)
    def getSubsystem(self):
        return self.subsystemList