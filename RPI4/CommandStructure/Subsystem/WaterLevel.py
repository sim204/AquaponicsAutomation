from . import Subsystem     #Importe le fichier Subsystem
from LowLevel import AnalogRead #Importe le fichier AnalogRead
from LowLevel import MotorController    #Importe le fichier MotorController

class WaterLevel(Subsystem.Subsystem):
    
    baseLength = 1#510  # To Change #La valeur de la longueur de l'aquarium en cm
    baseWidth = 1.478#265   # To Change #La valeur de la largeur de l'aquarium en cm
    baseArea = baseLength*baseWidth # En cm^2
    
    #Définit les variables initiales nécessaires pour le programme
    def __init__(self):
        #super().__init__()  #Prend les attributs de la classe mere
        self.analogPort=AnalogRead.AnalogRead(0)    #Est une instance d'AnalogRead. Le 0 est le port
        temp = self.analogPort.get()
        self.iteration = 0
        self.sensorValues = [temp,temp,temp,temp,temp,temp,temp]
        self.motorController=MotorController.MotorController(15,18,14)  #Est une instance de MotorControlle. Les chiffres sont les ports sur le PI
        
    def periodic(self):
        print(self.sensorValues,self.getLevel())
        pass

    #La methode servant à savoir si les moteurs doivent ajouter de l'eau ou non
    def addWater(self, rate):
        self.motorController.setPercentage(rate)

    #Lit le capteur du niveau d'eau et transforme la valeur
    def getLevel(self):
        # rate of change: -150.75 mm/V
        # analog to volts = 1023/5V 
        # constant: 629.01 mm
        # Height (in mm) = -150.75*(1023*analog value/5) + 629.01
        self.sensorValues[self.iteration] = self.analogPort.get()
        sumation = 0
        for i in self.sensorValues:
            sumation = sumation + i
        sumation = sumation - min(self.sensorValues) - max(self.sensorValues)
        sumation = sumation/(len(self.sensorValues)-2)
        temp = -155.3333*(5*sumation/1023) + 678.93333 #To Adjust
        self.iteration = self.iteration + 1
        if self.iteration == len(self.sensorValues):
            self.iteration = 0
        return temp #To Adjust

    #Calcule le niveau d'eau dans l'aquarium
    def getVolume(self):
        return WaterLevel.baseLength*WaterLevel.baseWidth*self.getLevel()