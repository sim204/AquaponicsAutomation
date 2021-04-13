from . import Command       #Importe le module Command
from CommandStructure.Subsystem import WaterLevel   #Importe le module WaterLevel
import time

#Cette classe sert à calculer les ajustements du niveau d'eau de l'aquarium
class AdjustWaterLevel(Command.Command):
    idealWaterLevel = 270 #In cm
    
    #Définit les variables initiales nécessaires pour le programme
    def __init__(self, waterLevelSubsystem):
        super().__init__()  #Prend les attributs de la classe mere
        super().addSubsystem(waterLevelSubsystem) #
        self.waterLevel = waterLevelSubsystem  #Prend une copie d'un instance de subsystem
    
    #Initialise la commande quand elle est scheduled par le Scheduler
    def initialise(self):
        
        # Deadline = Time now + estimated time to fill
        # Estimated time to fill = volume missing/Fill Rate
        # Volume missing = missing height * base Area
        # Fill rate (max pump flow)= 100mL / 60sec

        self.deadLine = time.time() + ((AdjustWaterLevel.idealWaterLevel - self.waterLevel.getLevel())*WaterLevel.WaterLevel.baseArea)/(100/60)
        
    #Execute l'ajout de l'eau avec les moteurs
    def execute(self):
        self.waterLevel.addWater(1)
    
    #Regarde si le niveau de l'eau est assez haut ou si trop de temps est passe depuis l'execution de l'eau
    def isFinish(self):
        return (self.waterLevel.getLevel() > AdjustWaterLevel.idealWaterLevel) or (time.time() > self.deadLine)

    #Eteint l'eau
    def end(self,isInterrupt):
        self.waterLevel.addWater(0)
