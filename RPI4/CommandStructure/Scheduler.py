from CommandStructure.Subsystem import Subsystem
from CommandStructure.Command import Command
from CommandStructure.Trigger import Trigger

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
        if isinstance(subsystem, Subsystem.Subsystem):
            self._subsystems.update({subsystem:None})
        else:
            print("A non subsystem was attempted to be added to the subsystem list")
    def scheduleCommand(self, command): #logic verified
        if isinstance(command, Command.Command):
            self._toBeScheduledCommands.append(command)
        else:
            print("A non Command was attempted to be scheduled")
    def addTrigger(self,trigger):
        if isinstance(trigger,Trigger.Trigger) and isinstance(trigger.getCommand(), Command.Command) :
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
            
        if command.getSubsystem() is not None and command in list(self._subsystems.values()):
            #command.getSubsystem() in list(self._subsystems.keys())
            tempSchedulerKnownedSubsystems = list(self._subsystems.keys())
            for requiredSubsystems in command.getSubsystem():
                if requiredSubsystems in tempSchedulerKnownedSubsystems:
                    self._subsystems[requiredSubsystems] = None
            
            
    
    def removeTrigger(self, trigger):
        if trigger in self._triggers:
            self.removeCommand(trigger.getCommand())
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
            1- Check if command is already scheduled (memory reference is exactly the same)
            2- Check if Command has subsystem requirements
                2.1- if it so, check if subsystem exit and if it is currently running a command
                    2.1.1 - if so, remove interrupt current command and replace the command
            3- add commands to list
            4- run commands
        """
        for toBeScheduledCommand in self._toBeScheduledCommands: #logic verified
            commandAlreadyExist = False
            for scheduledCommand in self._scheduledCommands: #check if command is already scheduled
                if toBeScheduledCommand == scheduledCommand:
                    self._toBeScheduledCommands.remove(toBeScheduledCommand)
                    commandAlreadyExist = True
                    break
            if not commandAlreadyExist:
                subsystemUsed = toBeScheduledCommand.getSubsystem()
                currentSubsystems =  list(self._subsystems.keys())
                if len(subsystemUsed) != 0 : #check if Command requires a Subsystem
                    for i in subsystemUsed:
                        if i is None or not i in currentSubsystems: # if required subsystem is null or it doesn't exist, skip
                            continue
                        currentScheduledCommand = self._subsystems[i]
                        if currentScheduledCommand is not None: #check if required Subsystem is currently running a Command
                            print(self._subsystems[i])
                            self.removeCommand(self._subsystems[i])
                        self._subsystems[i] = toBeScheduledCommand
                toBeScheduledCommand.initialise()
                self._scheduledCommands.append(toBeScheduledCommand)
                print(toBeScheduledCommand)
                self._toBeScheduledCommands.remove(toBeScheduledCommand)

        for scheduledCommand in self._scheduledCommands: # run scheduled commands
            if scheduledCommand.isFinish(): # if command is finished, call end() and remove from the scheduled command list
                self.removeCommand(scheduledCommand, False)
            else:
                scheduledCommand.execute()        
            
