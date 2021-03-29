import RPi.GPIO as GPIO

class DigitalWrite:
    def __init__(self, channel):
        self.channel = channel
        self.state = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.OUT)
    def setState(self, state):
        self.state = state
        GPIO.output(self.channel, state)
    def get(self):
        return self.state
        