from . import Command       #Importe le fichier Command
from CommandStructure.Subsystem import WaterLevel   #Importe le fichier WaterLevel
import time     #Importe le temps

#Cette classe sert à calculer les ajustements du niveau d'eau de l'aquarium
class AdjustWaterLevel(Command):
    #Définit les variables initiales nécessaires pour le programme
    def __init__(self,waterLevel):
        super().__init__()  #Prend les attributs de la classe mere
        self.waterLevel=waterLevel  #Prend la valeur du niveau d'eau de l'aquarium
        self.minWater=20    #Est la valeur minimale que l'aquarium peut contenir en pouces

    #Initialise la commande quand elle est scheduled par le Scheduler
    def initialise(self):
        self.tempsInitial=time.time()   #Prend le temps au moment où le Scheduler le demande
        self.deltaTemps=self.minWater - self.waterLevel.getVolume()/(100/60)    #Le temps nécessaire pour remplir l'eau au niveau max
    
    #Execute l'ajout de l'eau avec les moteurs
    def execute(self):
        self.waterLevel.addWater(1)
    
    #Regarde si le niveau de l'eau est assez haut ou si trop de temps est passe depuis l'execution de l'eau
    def isFinish(self):
        return (self.waterLevel.getLevel() > self.minWater) or (time.time() > (self.tempsInitial + self.deltaTemps))

    #Eteint l'eau
    def end(self,isInterrupt):
        self.waterLevel.addWater(0)
