import RPi.GPIO as GPIO

# Set GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Define button pins
buttons = [26, 19, 13, 6]

# Set button pins as input
GPIO.setup(buttons, GPIO.IN)

# Function to be called when button is pressed
def button_pressed(channel):
    print("Button is pressed on channel {}".format(channel))

# Add an event listener for falling edge (button press) on each button pin
for pin in buttons:
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_pressed, bouncetime=200)

try:
    # Keep the program running indefinitely (optional, can be replaced with your main program)
    while True:
        # Do other stuff here...
        pass

# Clean up GPIO on program exit
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting...')
except Exception as e:
    print('An error occurred:', e)
    GPIO.cleanup()
