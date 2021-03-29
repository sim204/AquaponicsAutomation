from . import Subsystem     #Importe le fichier Subsystem
from LowLevel import AnalogRead #Importe le fichier AnalogRead
from LowLevel import MotorController    #Importe le fichier MotorController

class WaterLevel(Subsystem):
    baseLength=36   #La valeur de la longueur de l'aquarium
    baseWidth=15    #La valeur de la largeur de l'aquarium
    
    #Définit les variables initiales nécessaires pour le programme
    def __init__(self):
        super().__init__()  #Prend les attributs de la classe mere
        self.analogPort=AnalogRead.AnalogRead(0)    #Est une instance d'AnalogRead. Le 0 est le port
        self.motorController=MotorController.MotorController(15,18,14)  #Est une instance de MotorControlle. Les chiffres sont les ports sur le PI
    
    def periodic(self):
        pass

    #La methode servant à savoir si les moteurs doivent ajouter de l'eau ou non
    def addWater(self, rate):
        #Si le pourcentage de la vitesse de débit est plus eleve que 0, active les moteurs
        if rate > 0:
            self.motorController.setPercentage(rate)
        #Sinon, permet une desactivation automatique en cas d'erreur
        else:
            self.motorController.setPercentage(0)

    #Lit le capteur du niveau d'eau et transforme la valeur
    def getLevel(self):
        return self.analogPort.get()/1023

    #Calcule le niveau d'eau dans l'aquarium
    def getVolume(self):
        return baseLength*baseWidth*self.getLevel()