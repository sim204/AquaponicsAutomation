from . import Subsystem
import time
import board
import busio
import adafruit_veml7700

#Code de lecture de Lumière fortement inspiré par et basé sur:
#https://learn.adafruit.com/adafruit-veml7700/python-circuitpython
class LightLevel(Subsystem.Subsystem):
    
    #Constructeur de LightLevel
    def __init__(self):
        self.i2cSensor = adafruit_veml7700.VEML7700(busio.I2C(board.SCL, board.SDA))
        pass

    #Prend le niveau de la lumiere periodiquement
    def periodic(self):
        #print("lux: ",self.getLightLevel())
        self.getLightLevel()
        pass
    
    #@return la valeur du niveau de la lumiere en lux
    def getLightLevel(self):
        return self.i2cSensor.lux 
        
