import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

output_pin = 17
input_pin = 21

# Set up GPIO pins as inputs
GPIO.setup(output_pin, GPIO.OUT)
# GPIO.setup(input_pin, GPIO.IN)
    
try:
    while True:
        GPIO.output(output_pin, GPIO.HIGH)
        # Read input value
        # input_value = GPIO.input(input_pin)
        # print("Input value:", input_value)
        
        time.sleep(.5)
        GPIO.output(output_pin, GPIO.LOW)
        time.sleep(.5)
        # GPIO.output(output_pin, GPIO.LOW)
        # input_value = GPIO.input(input_pin)
        # print("Input value:", input_value)
        # time.sleep(1)
        # Add a delay to avoid flooding the terminal
        


except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting button thread...')
except Exception as e:
    print('An error occurred in the button thread:', e)
    GPIO.cleanup()
