import Deserialise
import time

class AnalogRead:
    
    def __init__(self, AnalogPort = -1):
        self.analogPort = AnalogPort
    def get(self):
        if(self.analogPort != -1):
            return Deserialise.Deserialise.getInstance().readPort(self.analogPort)
        else:
            return None
if False:
    test = AnalogRead(0)
    test2 = Deserialise.Deserialise.getInstance()
    while True:
        test2.update()
        print(test.get())
        time.sleep(0.5)
    