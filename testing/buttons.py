import RPi.GPIO as GPIO
import threading

def gpio_init():
    GPIO.setmode(GPIO.BCM)

    # Define the pins for push buttons
    buttons = [26,19,13,6,24] 
    GPIO.setup(buttons, GPIO.IN)
    GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        if channel == 19:
            print('Increase volume button pressed')
            # tts.increase_volume()

        if channel == 13:
            print('Decrease volume button pressed')
            # tts.decrease_volume()
            
        if channel == 26 or channel == 24:
            print('Reclassify button pressed')
            # abort_audio()
            
        if channel == 6:
            print('Shutdown button pressed')
            # shutdown()
        
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.RISING, callback=button_pressed, bouncetime=200)

if __name__ == "__main__":
    try:
        gpio_init()  # Initialize GPIO
        while True:
            pass  # Keep the program running
            
    except KeyboardInterrupt:
        print("Exiting program.")
        GPIO.cleanup()  # Clean up GPIO pins on program exit
    finally:
        GPIO.cleanup()  # Clean up GPIO pins on program exit
    
        