import RPi.GPIO as GPIO

class PWMWrite:
    def __init__(self, channel):
        self.p = GPIO.PWM(channel, 100)
        self.p.start(0)
    def set(self, dc):
        self.p.ChangeDutyCycle(dc)
    def stop(self):
        self.p.ChangeDutyCycle(0)