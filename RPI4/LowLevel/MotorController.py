import DigitalWrite
import PWMWrite
import RPi.GPIO as GPIO

class MotorController():
    def __init__(self, channel1, channel2, channel3):
        self.IN1=DigitalWrite(channel1)
        self.IN2=DigitalWrite(channel2)
        self.IN2.set(GPIO.LOW)
        self.ENA=PWMWrite(channel3)

    def setPercentage(percentage):
        self.ENA.set(percentage)

    def motorStart():
        self.IN1.set(GPIO.HIGH)

    def motorStop():
        self.IN1.set(GPIO.LOW)
