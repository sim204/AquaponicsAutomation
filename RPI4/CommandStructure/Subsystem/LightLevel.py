from . import Subsystem
import time
import board
import busio
import adafruit_veml7700
"""
Code de lecture de Lumière fortement inspiré par et basé sur:
https://learn.adafruit.com/adafruit-veml7700/python-circuitpython
"""
class LightLevel(Subsystem.Subsystem):
    
    def __init__(self):
        self.i2cSensor = adafruit_veml7700.VEML7700(busio.I2C(board.SCL, board.SDA))
        pass
    def periodic(self):
        print("lux: ",self.getLightLevel())
        
    def getLightLevel(self):
        return self.i2cSensor.lux 
        
