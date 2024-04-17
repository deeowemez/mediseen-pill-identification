import RPi.GPIO as GPIO
import threading

def gpio_init():
    GPIO.setmode(GPIO.BCM)

    # Define the pins for push buttons
    buttons = [26,19,13,6] 
    GPIO.setup(buttons, GPIO.IN)
    # GPIO.setup(21, GPIO.OUT)
    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        # if channel == 26:
        #     tts.increase_volume()

        # if channel == 19:
        #     tts.decrease_volume()
            
        # if channel == 13:
        #     abort_audio()
            
        # if channel == 6:
        #     shutdown()
        
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

if __name__ == "__main__":
    try:
        button_thread = threading.Thread(target=gpio_init, daemon=True)
        button_thread.start()
    
    except Exception as e:
        GPIO.cleanup()
        