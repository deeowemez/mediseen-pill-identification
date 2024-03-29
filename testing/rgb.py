import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pins for RGB LED
red_pin = 22
green_pin = 27
blue_pin = 17

# Set up PWM channels
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

red_pwm = GPIO.PWM(red_pin, 100)  # PWM frequency for red LED
green_pwm = GPIO.PWM(green_pin, 100)  # PWM frequency for green LED
blue_pwm = GPIO.PWM(blue_pin, 100)  # PWM frequency for blue LED

red_pwm.start(0)  # Start PWM with 0% duty cycle
green_pwm.start(0)
blue_pwm.start(0)

# Define a function to set the color of the RGB LED
def set_color(red, green, blue):
    red_pwm.ChangeDutyCycle(red)
    green_pwm.ChangeDutyCycle(green)
    blue_pwm.ChangeDutyCycle(blue)

# Main program
if __name__ == "__main__":
    try:
        while True:
            # set_color(30, 100, 35)  # option 1
            # set_color(60, 100, 35)  # 2
            set_color(70, 100, 40)  # 3
            # time.sleep(1)
            # set_color(0, 100, 0)  # Green
            # time.sleep(1)
            # set_color(0, 0, 100)  # Blue
            # time.sleep(1)
            # set_color(100, 100, 0)  # Yellow
            # time.sleep(1)
            # set_color(100, 0, 100)  # Magenta
            # time.sleep(1)
            # set_color(0, 100, 100)  # Cyan
            # time.sleep(1)
    except KeyboardInterrupt:
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()
