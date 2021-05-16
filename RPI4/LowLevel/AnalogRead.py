from . import Deserialise

#Cette classe s'occupe de lire une seule port analogue
class AnalogRead:
    #Constructeur de la classe AnalogRead
    #@param AnalogPort le numéro du port analogue
    def __init__(self, AnalogPort = -1):
        self.analogPort = AnalogPort
    #Méthode qui retour la valeur du port analogue
    #@return la valeur du port entre 0 et 1023 (0 étant 0 V et 1023 étant 5V)
    def get(self):
        if(self.analogPort != -1):
            return Deserialise.Deserialise.getInstance().readPort(self.analogPort)
        else:
            return None   