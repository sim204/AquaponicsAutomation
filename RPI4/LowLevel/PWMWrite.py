import RPi.GPIO as GPIO
import math
#Classe qui gère les sorties PWM (pourcentage), c'est une simplification de la librarie GPIO, dans le but de rendre le code plus simple à comprendre
class PWMWrite:
    #Constructeur de PWMWrite
    #@param channel le port d'écriture
    def __init__(self, channel):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel,GPIO.OUT)
        self.p = GPIO.PWM(channel, 100)
        self.p.start(0)
    #Méthode qui fait l'écriture du signal PWM au port d'écriture établie
    #@param dc le Duty-Cycle (le pourcentage de [0,1])
    def setDutyCycle(self, dc):
        setVal = min(abs(dc),1.0) #limite automatiquement la 
        setVal = setVal * 100        
        self.p.ChangeDutyCycle(math.floor(setVal))
    #Méthode qui écrit un signal PWM de valeur 0 sur le port d'écriture établie 
    def stop(self):
        self.p.ChangeDutyCycle(0)