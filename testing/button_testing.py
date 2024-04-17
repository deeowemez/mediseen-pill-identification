import RPi.GPIO as GPIO
import time

button = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button, GPIO.IN)


try:
    while True:
        print (GPIO.input(button))
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()