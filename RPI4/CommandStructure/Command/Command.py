class Command:
    def __init__(self):
        self.subsystemList = []
        pass
    def initialise(self):
        pass
    def execute(self):
        pass
    def isFinish(self):
        pass
    def end(self,isInterrupt):
        pass
    def addSubsystem(self,subsystem):
        self.subsystemList.append(subsystem)
    def getSubsystem(self):
        return self.subsystemList