from . import Subsystem     
from LowLevel import AnalogRead
from LowLevel import MotorController

#Classe qui relie le haut et bas niveau
#Dans le cas de WaterLevel, elle gère le capteur de niveau d'eau et le contrôlleur de moteur qui contrôlle la pompe
class WaterLevel(Subsystem.Subsystem):
    
    baseLength = 1 #La longueur de l'aquarium en mm
    baseWidth = 1.478 #La largeur de l'aquarium en mm
    baseArea = baseLength*baseWidth # l'aire de la base de l'aquarium en mm^2
    
    #Constructeur de WaterLevel
    def __init__(self):
        #super().__init__()
        self.analogPort=AnalogRead.AnalogRead(0) #Création d'un port analogue au port 0
        temp = self.analogPort.get()
        self.iteration = 0 #compteur pour le filtre de capteur
        self.sensorValues = [temp,temp,temp,temp,temp,temp,temp] #données récoltées pour le filtre de capteur
        self.motorController=MotorController.MotorController(15,18,14) #Création d'un contrôlleur de moteur pour controller la pompe
    #mise à jour des valeurs de capteur de niveau d'eau
    def periodic(self):
        #print(self.sensorValues,self.getLevel())
        self.getLevel()
        pass

    #Cette méthode permet d'activer le niveau d'eau
    #@param rate le pourcentage de la vitesse (de [-1,1])
    def addWater(self, rate):
        self.motorController.setPercentage(rate)

    #Lit le capteur du niveau d'eau et converti le voltage du capteur en hauteur de niveau d'eau
    #@return the niveau d'eau en mm
    def getLevel(self):
        # Pente calculée: -155.3333 mm/V
        # analog à volts = 1023/5V 
        # ordonnée à l'origine calculée: 678.93333 mm
        # hauteur (en mm) = -155.3333*(1023*valeur analogue/5) + 678.93333
        self.sensorValues[self.iteration] = self.analogPort.get() #lecture de voltage

        #filtre simple qui prend en considération les sept dernières valeurs récoltée
        #Elle rejette la valeur la plus grande et la valeur la plus petite et elle fait la moyenne des cinq restants
        sumation = 0
        for i in self.sensorValues:
            sumation = sumation + i
        sumation = sumation - min(self.sensorValues) - max(self.sensorValues)
        sumation = sumation/(len(self.sensorValues)-2) 
        
        temp = -155.3333*(5*sumation/1023) + 678.93333 
        
        self.iteration = self.iteration + 1
        if self.iteration == len(self.sensorValues):
            self.iteration = 0
        return temp

    #@return le volume estimée de l'aquarium en mm^3
    def getVolume(self):
        return WaterLevel.baseLength*WaterLevel.baseWidth*self.getLevel()