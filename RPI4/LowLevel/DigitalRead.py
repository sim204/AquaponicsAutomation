import RPi.GPIO as GPIO

class DigitalRead:
    def __init__(self, channel):
        self.channel = channel
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.IN)
    def get(self):
        return GPIO.input(self.channel)