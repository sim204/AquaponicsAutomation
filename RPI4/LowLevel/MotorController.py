import DigitalWrite
import PWMWrite
import RPi.GPIO as GPIO

class MotorController():
    def __init__(self, forwardPin, backwardPin, PWMPin):
        self.IN1=DigitalWrite(forwardPin)
        self.IN1.set(GPIO.LOW)
        self.IN2=DigitalWrite(backwardPin)
        self.IN2.set(GPIO.LOW)
        self.ENA=PWMWrite(PWMPin)
        self.percentage=0

    def setPercentage(self, percentage):
        self.percentage=percentage
        if percentage < 0:
            self.ENA.set(-percentage)
            self.IN1.set(GPIO.LOW)
            self.IN2.set(GPIO.HIGH)
        elif percentage > 0:
            self.ENA.set(percentage)
            self.IN1.set(GPIO.HIGH)
            self.IN2.set(GPIO.LOW)
        else:
            self.motorStop()
    
    def getPercentage(self):
        return self.percentage

    def motorStop(self):
        self.IN1.set(GPIO.LOW)
        self.IN2.set(GPIO.LOW)
        self.percentage=0
