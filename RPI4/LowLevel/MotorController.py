import DigitalWrite     #Importe le fichier DigitalWrite
import PWMWrite         #Importe le fichier PWMWrite
import RPi.GPIO as GPIO #Importe le fichier travailler sur le PI

#Cette classe sert a allumer ou eteindre chacun des moteurs du projet
class MotorController():
    #Definit les variables initiales necessaires pour le programme
    def __init__(self, forwardPin, backwardPin, PWMPin):
        self.IN1=DigitalWrite(forwardPin)   #Est la pin pour pousser l'eau
        self.IN1.set(GPIO.LOW)      #Met la pin a OFF
        self.IN2=DigitalWrite(backwardPin)  #Est la pin pour tirer l'eau
        self.IN2.set(GPIO.LOW)      #Met la pin a OFF
        self.ENA=PWMWrite(PWMPin)   #Est la pin pour savoir la vitesse de rotation des moteurs
        self.percentage=0   #Est la vitesse des moteurs

    #Controle la puissance des moteurs et leurs direction de rotation
    def setPercentage(self, percentage):
        self.percentage=percentage

        #Si le pourcentage est sous 0, tourne pour aspirer l'eau
        if percentage < 0:
            self.ENA.set(-percentage)   #Le moins est la pour avoir une valeur de puissance
            self.IN1.set(GPIO.LOW)
            self.IN2.set(GPIO.HIGH)
        
        #Si le pourcentage est au dessus de 0, tourne pour tirer de l'eau
        elif percentage > 0:
            self.ENA.set(percentage)
            self.IN1.set(GPIO.HIGH)
            self.IN2.set(GPIO.LOW)
        
        #Si le pourcentage est egal a 0, eteint le moteur
        else:
            self.motorStop()
    
    #Retourne la valeur du pourcentage
    def getPercentage(self):
        return self.percentage

    #Eteint le moteur
    def motorStop(self):
        self.IN1.set(GPIO.LOW)
        self.IN2.set(GPIO.LOW)
        self.percentage=0
