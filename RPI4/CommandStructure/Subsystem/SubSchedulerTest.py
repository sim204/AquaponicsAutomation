from . import Subsystem

class SubSchedulerTest(Subsystem.Subsystem):
    def __init__(self):
        super().__init__()
        self.test = 0
    
    def periodic(self):
        self.test = self.test + 1
        #print(self.test)