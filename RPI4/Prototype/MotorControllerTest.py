import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
percentPin = 16
forwardPin = 12
backwardPin = 11
GPIO.setup(percentPin, GPIO.OUT)
GPIO.setup(forwardPin, GPIO.OUT)
GPIO.setup(backwardPin, GPIO.OUT)

p = GPIO.PWM(percentPin, 50)  # channel=12 frequency=50Hz
p.start(0)
#while True:
GPIO.output(forwardPin, True)
GPIO.output(backwardPin, False)
p.ChangeDutyCycle(100)
    
time.sleep(5)

GPIO.output(forwardPin, False)
GPIO.output(backwardPin, True)
p.ChangeDutyCycle(100)
time.sleep(5)
GPIO.output(backwardPin, False)
