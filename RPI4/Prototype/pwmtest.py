import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
pinout = 16
GPIO.setup(pinout, GPIO.OUT)

p = GPIO.PWM(pinout, 100)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()