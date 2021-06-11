from . import Subsystem     
from LowLevel import AnalogRead
from LowLevel import MotorController
import LinearInterpolation
#Classe qui relie le haut et bas niveau
#Dans le cas de WaterLevel, elle gere le capteur de niveau d'eau et le contrôlleur de moteur qui controlle la pompe
class WaterLevel(Subsystem.Subsystem):
    
    baseLength = 1 #La longueur de l'aquarium en mm
    baseWidth = 1.478 #La largeur de l'aquarium en mm
    baseArea = baseLength*baseWidth # l'aire de la base de l'aquarium en mm^2
    xValue = [4.098113,4.07625,4.071358,4.05181,4.0271,3.9932,3.97849,3.69013,3.63636,3.55327,3.5109,3.45552,3.35777,3.24047,3.17693,3.11828,2.96188,2.67351,2.50733]
    yValue = [0,30,40,60,80,100,120,140,150,160,180,200,220,240,263,290]

    #Constructeur de WaterLevel
    def __init__(self):
        #super().__init__()
        self.analogPort=AnalogRead.AnalogRead(0) #Création d'un port analogue au port 0
        temp = self.analogPort.get()
        self.iteration = 0 #compteur pour le filtre de capteur
        self.sensorValues = [temp,temp,temp,temp,temp,temp,temp] #données récoltées pour le filtre de capteur
        self.motorController=MotorController.MotorController(15,18,14) #Création d'un contrôlleur de moteur pour controller la pompe
        self.VoltToMM = LinearInterpolation.LinearInterpolation(xValue,yValue)
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
        

        #filtre simple qui prend en considération les sept dernières valeurs récoltée
        #Elle rejette la valeur la plus grande et la valeur la plus petite et elle fait la moyenne des cinq restants
        sumation = 0
        for i in self.sensorValues:
            sumation = sumation + i
        sumation = sumation - min(self.sensorValues) - max(self.sensorValues)
        sumation = sumation/(len(self.sensorValues)-2) 

        voltage = sumation*5.0/1023.0 # analog à volts = 5v/1023
        temp = self.VoltToMM.getY(voltage)

        self.iteration = self.iteration + 1
        if self.iteration == len(self.sensorValues):
            self.iteration = 0
        return temp

    #@return le volume estimée de l'aquarium en mm^3
    def getVolume(self):
        return WaterLevel.baseLength*WaterLevel.baseWidth*self.getLevel()