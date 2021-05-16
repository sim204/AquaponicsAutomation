import RPi.GPIO as GPIO

#Classe qui gère les sorties digitaux (Vrai/Faux, 5V/0V), c'est une simplification de la librarie GPIO, dans le but de rendre le code plus simple à comprendre
class DigitalWrite:
    #Constructeur de DigitalWrite
    #@param channel le port d'écriture (GPIO# et non le # de pin sur le Board)
    def __init__(self, channel):
        self.channel = channel
        self.state = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.OUT)

    #Méthode qui fait l'écriture au port d'écriture établie
    #@param setState l'état dans laquelle il faut mettre le port (Vrai ou Faux)
    def setState(self, state):
        self.state = state
        GPIO.output(self.channel, state)
    #Méthode qui retourne l'état actuel du port
    #@return vrai ou faux
    def get(self):
        return self.state
        