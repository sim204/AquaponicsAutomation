import CommandStructure.Subsystem
import CommandStructure.Command
import CommandStructure.Trigger

class Scheduler:
    __instance = None
    def __init__(self):
        self._subsystems = dict()
        self._triggers = []
        self._toBeScheduledCommands = []
        self._scheduledCommands = []
    @staticmethod
    def getInstance():
        if Scheduler.__instance is None:
            Scheduler.__instance = Scheduler()
        return Scheduler.__instance

    def addSubsystem(self, subsystem):
        if subsystem is Subsystem.Subsystem:
            self._subsystems.update({subsystem:None})
        else:
            print("A non subsystem was attempted to be added to the subsystem list")
    def scheduleCommand(self, command):
        if command is Command.Command:
            self._toBeScheduledCommands.append(command)
        else:
            print("A non Command was attempted to be scheduled")
    def addTrigger(self,trigger):
        if command is Trigger.Trigger and trigger.getCommand is Command.Command:
            self._triggers.append(trigger)
        else:
            print("A non Trigger was attempted to be added to the Trigger list")

    def removeSubsystem(self, subsystem):
        if subsystem in self._subsystems:
            self._subsystems.pop(subsystem)

    def removeCommand(self, command, isFinish = True):
        if command in self._scheduledCommands:
            command.end(isFinish)
            self._scheduledCommands.remove(command)
        if command in self._toBeScheduledCommands:
            self._toBeScheduledCommands.remove(command)
        if command.getSubsystem() is not None and command.getSubsystem() in list(self._subsystems.keys()) and command in list(self._subsystems.values()):
            self._subsystems[command.getSubsystem()] = None
    
    def removeTrigger(self, trigger):
        self.removeCommand(trigger.getCommand())
        if trigger in self._triggers:
            self._triggers.remove(trigger)

    def run(self):
        """
            1- update Sub.periodic()
            2- schedule trigger
            3- associate Command to sub
            4- run commands
        """
        for i in self._subsystems: #call periodic() for all subsystems
            i.periodic()
        
        for i in self._triggers: #check trigger and if get() returns true, add to the schedule Command list
            if i.get():
                self._toBeScheduledCommands.append(i.getCommand())
        """
            1- check if command is already scheduled
            2- Check if subsystem exist
                2.1- if it does, check if subsystem is currently running a command
                    2.1.1 - if so, remove interrupt current command and replace the command
            3- add commands to list (also )
            4- run commands
        """
        for toBeScheduledCommand in self._toBeScheduledCommands:
            commandAlreadyExist = False
            for scheduledCommand in self._scheduledCommands: #check if command is already scheduled
                if toBeScheduledCommand is scheduledCommand:
                    self._toBeScheduledCommands.remove(scheduledCommand)
                    commandAlreadyExist = True
                    break
            if commandAlreadyExist:
                continue
            currentSubsystem = toBeScheduledCommand.getSubsystem()
            if currentSubsystem is Subsystem.Subsystem: #check if Command requires a Subsystem
                if toBeScheduledCommand in list(self._subsystems.values()): #check if required Subsystem is currently running a Command
                    self.removeCommand(toBeScheduledCommand)
                    self._subsystems[currentSubsystem] = toBeScheduledCommand
            toBeScheduledCommand.initialise()
            self._scheduledCommands.append(toBeScheduledCommand)
        
        for scheduledCommand in self._scheduledCommands: # run scheduled commands
            if scheduledCommand.isFinish(): # if command is finished, call end() and remove from the scheduled command list
                self.removeCommand(scheduledCommand, True)
            else:
                scheduledCommand.execute()        
            
