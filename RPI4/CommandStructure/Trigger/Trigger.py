#Cette classe détermine lorsqu'il faut appeler un Command de façon automatique grâce au Trigger.get()
class Trigger():
    #Constructeur de Trigger
    #@command le Command qui devrait être appeller lorsque Trigger.get() == true
    def __init__(self, command):
        self.command = command
    #@return s'il faut appeller le Command
    def get(value):
        raise NotImplementedError
    #@return le Command à appeller
    def getCommand(self):
        return self.command
