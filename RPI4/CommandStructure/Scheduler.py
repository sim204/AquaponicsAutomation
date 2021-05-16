from CommandStructure.Subsystem import Subsystem
from CommandStructure.Command import Command
from CommandStructure.Trigger import Trigger

#Cette classe fait la gestion de l'éxécution du code, ainsi que la gestion de ressources (Subsystem et Commands)
class Scheduler:
    __instance = None
    
    #Constructeur de Scheduler
    def __init__(self):
        self._subsystems = dict() #dictionnaire de Subsystem
        self._triggers = [] #List de Trigger
        self._toBeScheduledCommands = [] #List de Commands en attente, PendingCommand (PCommand)
        self._scheduledCommands = [] #List de Command en exécution, RunningCommand (RCommand)

    #Méthode qui retourne une instance statique de Scheduler 
    @staticmethod
    def getInstance():
        if Scheduler.__instance is None:
            Scheduler.__instance = Scheduler()
        return Scheduler.__instance
    
    #Méthode qui ajoute un Subsystem au dictionnaire des Subsystems
    #@param subsystem un Subsystem à ajouter
    def addSubsystem(self, subsystem):
        if isinstance(subsystem, Subsystem.Subsystem):
            self._subsystems.update({subsystem:None})
        else:
            print("A non subsystem was attempted to be added to the subsystem dictionnary")
    
    #Méthode qui ajoute un Commands au List de Commands en attente (Pending Command, PCommand)
    #@param command PCommand à ajouter
    def scheduleCommand(self, command):
        if isinstance(command, Command.Command):
            self._toBeScheduledCommands.append(command)
        else:
            print("A non Command was attempted to be scheduled")
    #Méthode qui ajoute un Trigger au List de Trigger connu
    #@param trigger Trigger à ajouter
    def addTrigger(self,trigger):
        if isinstance(trigger,Trigger.Trigger) and isinstance(trigger.getCommand(), Command.Command) :
            self._triggers.append(trigger)
        else:
            print("A non Trigger was attempted to be added to the Trigger list")

    #Méthode qui enlève un Subsystem du dictionnaire de Subsystem
    #@param subsystem le subsystem(objet/addresse mémoire)  à enlever 
    def removeSubsystem(self, subsystem):
        if subsystem in self._subsystems:
            self._subsystems.pop(subsystem)

    #Méthode qui enlève un Command dy List PCommand, du List de Command en exécution (RunningCommand, RCommand) et du dictionnaire de Subsystem
    #@param command le Command(objet/addresse mémoire) à enlever 
    #@param isFinish si le Command est interrompu
    def removeCommand(self, command, isFinish = True):
        if command in self._scheduledCommands:
            command.end(isFinish)
            self._scheduledCommands.remove(command)
        if command in self._toBeScheduledCommands:
            self._toBeScheduledCommands.remove(command)
            
        if command.getSubsystem() is not None and command in list(self._subsystems.values()):
            #command.getSubsystem() in list(self._subsystems.keys())
            tempSchedulerKnownedSubsystems = list(self._subsystems.keys())
            for requiredSubsystems in command.getSubsystem(): #Un command peut avoir plusieur Subsystem requis
                if requiredSubsystems in tempSchedulerKnownedSubsystems:
                    self._subsystems[requiredSubsystems] = None
            
            
    #Méthode qui enlève un Trigger du List de Trigger connu
    #@param trigger trigger(objet/addresse mémoire) à enlever
    def removeTrigger(self, trigger):
        if trigger in self._triggers:
            self.removeCommand(trigger.getCommand())
            self._triggers.remove(trigger)

    #Méthode qui éxécute un cycle d'éxécution
    #En résumer :
    #1-Elle fait un appel à tous les Subsystem.periodic()
    #2-Elle vérifie les Triggers.get() == true pour ajouter leur Command à PCommand
    #3-Elle traite le List de PCommand (PCommand est _toBeScheduledCommands)
    #3-Elle traite le List de RCommand (RCommand est _scheduledCommands)
    def run(self):
        #1
        for i in self._subsystems: 
            i.periodic()
        #2
        for i in self._triggers: #check trigger and if get() returns true, add to the schedule Command list
            if i.get():
                self._toBeScheduledCommands.append(i.getCommand())
        #3
        #3.1 En résumer, vérifie s'il y a répétition
        for toBeScheduledCommand in self._toBeScheduledCommands: #pour chaque PCommand dans le List de PCommand
            commandAlreadyExist = False 
            for scheduledCommand in self._scheduledCommands: #Pour chaque Command dans RCommand
                if toBeScheduledCommand == scheduledCommand: #vérifie si l'instance de PCommand existe déjà dans RCommand
                    self._toBeScheduledCommands.remove(toBeScheduledCommand) #Si c'est le cas, il n'est pas nécessaire de refaire l'éxécution, puisque qu'elle exécute déjà en ce moment
                    commandAlreadyExist = True #"Tagger" ce Command comme "Non nécessaire"
                    break
            #3.2 En résumer, s'il n'y a pas répétition, vérifie les Commands requis
            if not commandAlreadyExist: #Si le Command n'est pas "tagger", passe aux autres vérifications
                subsystemUsed = toBeScheduledCommand.getSubsystem() 
                currentSubsystems =  list(self._subsystems.keys())
                if len(subsystemUsed) != 0 : #vérifie si PCommand requiert des Subsystem, si oui, il faut faire plus de vérification
                    for i in subsystemUsed: #Pour tout les Subsystems requis de PCommand
                        if i is None or not i in currentSubsystems: #Si, un Subsystem est None ou que le Subsystem n'est pas dans le dictionnaire des Subsystems, pass au prochain
                            continue
                        currentScheduledCommand = self._subsystems[i]
                        if currentScheduledCommand is not None: #Vérifie si le Subsystem requis est associé à une autre commande (donc si le value est None)
                            self.removeCommand(self._subsystems[i]) #Si oui, déassocie et enlève RCommand
                        self._subsystems[i] = toBeScheduledCommand # finalement, associe le PCommand au Subsystem correspondant
                #3.3 En résumer, tous est bon, donc déplace PCommand à RCommand
                toBeScheduledCommand.initialise() #Rendu ici, initie PCommand
                self._scheduledCommands.append(toBeScheduledCommand) #PCommand devient un RCommand (Étant dans le List de RCommand)
                self._toBeScheduledCommands.remove(toBeScheduledCommand)# PCommand se fait enlever du List de PCommand

        for scheduledCommand in self._scheduledCommands: #4
            if scheduledCommand.isFinish(): #Si Command.isFinish() == true, le RCommand a terminer, donc enlève le du List de RCommand et du dictionnaire de Subsystem 
                self.removeCommand(scheduledCommand, False)
            else:#Sinon, fait Command.execute()
                scheduledCommand.execute()        
            
