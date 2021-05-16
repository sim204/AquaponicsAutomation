import RPi.GPIO as GPIO
#Classe qui gère les entrées digitaux (Vrai/Faux, 5V/0V), c'est une simplification de la librarie GPIO, dans le but de rendre le code plus simple à comprendre
class DigitalRead:
    #Constructeur de DigitalRead
    #@param channel le port de lecture (GPIO# et non le # de pin sur le Board)
    def __init__(self, channel):
        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.IN)
    #Méthode qui fait la lecture au port de lecture établie
    #@return l'état dans laquelle le port est (Vrai ou Faux)
    def get(self):
        return GPIO.input(self.channel)