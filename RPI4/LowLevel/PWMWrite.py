import RPi.GPIO as GPIO
import math
class PWMWrite:
    def __init__(self, channel):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel,GPIO.OUT)
        self.p = GPIO.PWM(channel, 100)
        self.p.start(0)
        
    def setDutyCycle(self, dc):
        setVal = dc
        if dc > 1.0:
            setVal = 1.0
        elif dc < -1.0:
            setVal = -1.0
        setVal = setVal * 100        
        self.p.ChangeDutyCycle(math.floor(setVal))
    def stop(self):
        self.p.ChangeDutyCycle(0)