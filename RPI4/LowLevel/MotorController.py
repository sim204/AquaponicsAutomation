from . import DigitalWrite
from . import PWMWrite
import RPi.GPIO as GPIO
import math

#Cette classe sert à controller un moteur à partir du contrôlleur de moteur L298N
class MotorController():
    #Constructeur de MotorController
    #@param forwardPin Le Pin de la première direction(IN1 sur le L298N et le pin est le GPIO# et non le # du Board)
    #@param backwardPin Le pin de la direction opposée(IN2 sur le L298N et le pin est le GPIO# et non le # du Board)
    #@param PWMPin Le Pin sur lequel la vitesse peut être moduler (ENA le L298N et le pin est le GPIO# et non le # du Board)
    def __init__(self, forwardPin, backwardPin, PWMPin):
        self.IN1=DigitalWrite.DigitalWrite(forwardPin)
        self.IN1.setState(GPIO.LOW)
        self.IN2=DigitalWrite.DigitalWrite(backwardPin)
        self.IN2.setState(GPIO.LOW)
        self.ENA=PWMWrite.PWMWrite(PWMPin)
        self.percentage=0

    #Cette méthode permet d'activer un moteur à une vitesse spécifier (en pourcentage de [-1,1])
    #@param percentage le pourcentage de [-1,1] (pourcentage < 0 étant la direction opposée à pourcentage > 0)
    def setPercentage(self, percentage):
        self.percentage = percentage

        #Si le signe de percentage est négative, tourne dans la direction opposé
        if percentage < 0:
            self.IN1.setState(GPIO.LOW)
            self.IN2.setState(GPIO.HIGH)
        
        #Si le signe de percentage est positive, tourne dans la direction normale
        elif percentage > 0:
            self.IN1.setState(GPIO.HIGH)
            self.IN2.setState(GPIO.LOW)
        
        #Si le pourcentage est egal a 0, arrête le moteur
        else:
            self.motorStop()
        self.ENA.setDutyCycle(abs(percentage)) #si pourcentage n'est pas dans l'intervale, le pourcentage est automatiquement limité à 1
    
    #@return la valeur du pourcentage
    def getPercentage(self):
        return self.percentage

    #Éteint le moteur
    def motorStop(self):
        self.IN1.setState(GPIO.LOW)
        self.IN2.setState(GPIO.LOW)
        self.percentage=0
