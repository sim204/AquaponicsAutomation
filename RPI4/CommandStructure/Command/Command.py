class Command:
    def __init__(self):
        self.subsystemList = []
    def initialise(self):
        raise NotImplementedError
    def execute(self):
        raise NotImplementedError
    def isFinish(self):
        raise NotImplementedError
    def end(self,isInterrupt):
        raise NotImplementedError
    def addSubsystem(self,subsystem):
        self.subsystemList.append(subsystem)
    def getSubsystem(self):
        return self.subsystemList

