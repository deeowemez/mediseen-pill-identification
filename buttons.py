import RPi.GPIO as GPIO
import time

def classify():
    print('Classify button pressed')
    return True

def gpio_init():
    try:
        GPIO.setmode(GPIO.BCM)

        buttons = [26,19,13,6]

        # Set up GPIO pins as inputs
        GPIO.setup(buttons, GPIO.IN)
        
        def button_pressed(channel):
            print(f"Button is pressed on channel {channel}")
            
            if channel == 6:
                classify()

        for button in buttons:
            GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

    except Exception as e:
        print(f"An error occurred during GPIO initialization: {e}")

if __name__ == "__main__":
    try:
        gpio_init()
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Exiting button thread...')
    except Exception as e:
        print('An error occurred in the button thread:', e)
        GPIO.cleanup()
