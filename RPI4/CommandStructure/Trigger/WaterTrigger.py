from . import Trigger
import time
#Classe qui appelle automatiquement le Command AdjustWaterLevel
#Cette classe hérite de Trigger
class WaterTrigger(Trigger.Trigger):
    minLevel = 145 #le niveau d'eau minimale en mm
    minDelayBetweenTriggers = 60 #Le délai entre deux activations en seconde
    
    #Le constructeur de WaterTrigger 
    #@param subsystem Instance de WaterLevel
    #@param command Instance de AdjustWaterLevel
    def __init__(self, subsystem, command):
        super().__init__(command)
        self.command = command
        self.waterLevel = subsystem
        #Quand le programme commence, il y a un minimale délai de 5 secondes avant la première activation
        self.startTime = time.time()- WaterTrigger.minDelayBetweenTriggers + 5      
    #@return s'il faut appeller le Command pour activer l'ajustement de niveau d'eau
    def get(self):
        self.cond = (self.waterLevel.getLevel() > 0 and #vérification s'il y a une lecture valide du capteur
                     self.waterLevel.getLevel() < 300 and #vérification s'il y a une lecture valide du capteur
                    (self.waterLevel.getLevel() < WaterTrigger.minLevel) and #vérification du niveau d'eau
                    (time.time() - self.startTime >= WaterTrigger.minDelayBetweenTriggers) #vérification du délai d'activation
                    )
        if self.cond:
            self.startTime = time.time()
        #print("tried")
        return self.cond
