import RPi.GPIO as GPIO

class DigitalWrite:
    def __init__(self, channel):
        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.OUT)
    def set(self, state):
        GPIO.output(self.channel, state)