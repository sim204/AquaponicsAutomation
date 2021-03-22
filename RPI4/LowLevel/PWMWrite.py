import RPi.GPIO as GPIO

class PWMWrite:
    def __init__(self, channel):
        self.p = GPIO.PWM(channel, 100)
        p.start(0)
    def set(dc):
        p.ChangeDutyCycle(dc)
    def stop():
        p.ChangeDutyCycle(0)