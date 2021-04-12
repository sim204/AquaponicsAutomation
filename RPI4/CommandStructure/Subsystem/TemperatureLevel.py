#from . import Subsystem
import Subsystem
import glob
import time
"""
Code de lecture de température fortement inspiré par et basé sur:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing?view=all#software
"""
class TemperatureLevel(Subsystem.Subsystem):
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    
    def __init__(self):
        pass
    def periodic(self):
        self.read_temp()
    def read_temp_raw(self):
        f = open(TemperatureLevel.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:] #read the number starting from index equals_pos + 2 to the end of the line
            temp_c = float(temp_string) / 1000.0
            return temp_c
"""def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES': #take first line of the file, remove spaces, check if 3 last characters of line spells 'YES'
            time.sleep(0.2) #if not retake the temperature
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c, temp_f
    """
