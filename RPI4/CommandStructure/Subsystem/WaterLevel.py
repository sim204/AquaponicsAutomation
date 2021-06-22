from . import Subsystem     
from LowLevel import AnalogRead
from LowLevel import MotorController
import LinearInterpolation
#Classe qui relie le haut et bas niveau
#Dans le cas de WaterLevel, elle gere le capteur de niveau d'eau et le contrôlleur de moteur qui controlle la pompe
class WaterLevel(Subsystem.Subsystem):
    
    baseLength = 6 #La longueur de l'aquarium en cm
    baseWidth = 30 #La largeur de l'aquarium en cm
    baseArea = baseLength*baseWidth # l'aire de la base de l'aquarium en cm^2
    baseUltrasonicOffset = 191
    #Constructeur de WaterLevel
    def __init__(self):
        #super().__init__()
        self.analogPort=AnalogRead.AnalogRead(6) #Création d'un port analogue au port 0
        temp = self.analogPort.get()
        self.iteration = 0 #compteur pour le filtre de capteur
        self.sensorValues = [temp,temp,temp,temp,temp,temp,temp] #données récoltées pour le filtre de capteur
        self.motorController=MotorController.MotorController(15,18,14) #Création d'un contrôlleur de moteur pour controller la pompe
        
    #mise à jour des valeurs de capteur de niveau d'eau
    def periodic(self):
        print(self.sensorValues,self.getLevel())
        self.getLevel()
        pass

    #Cette méthode permet d'activer le niveau d'eau
    #@param rate le pourcentage de la vitesse (de [-1,1])
    def addWater(self, rate):
        self.motorController.setPercentage(rate)

    #Lit le capteur du niveau d'eau et converti le voltage du capteur en hauteur de niveau d'eau
    #@return the niveau d'eau en mm
    def getLevel(self):
        self.sensorValues[self.iteration] = self.analogPort.get() #lecture de voltage
        #filtre simple qui prend en considération les sept dernières valeurs récoltées
        #Elle rejette la valeur la plus grande et la valeur la plus petite et elle fait la moyenne des cinq restants
        sumation = 0
        for i in self.sensorValues:
            if i is None:
                i = 0
            sumation = sumation + i
        sumation = sumation - min(self.sensorValues) - max(self.sensorValues)
        sumation = sumation/(len(self.sensorValues)-2) 

        self.iteration = self.iteration + 1
        if self.iteration == len(self.sensorValues):
            self.iteration = 0
        return round(WaterLevel.baseUltrasonicOffset - sumation,2)

    #@return le volume estimée de l'aquarium en cm^3 (1 cm^3 = mL)
    def getVolume(self):
        return WaterLevel.baseArea*(self.getLevel()/10)