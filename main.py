#!/usr/bin/env python

# Import libraries for running model
import model
import time

# Import libraries for tts
import tts

# Import libraries for gui
import gui

# Import libraries for accessing GPIO pins
# import buttons
import RPi.GPIO as GPIO
import threading

# Import libraries for taking pictures
import webcam

# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

# Initialize buttons values
button_classify = False

def gpio_init():
    GPIO.setmode(GPIO.BCM)

    buttons = [26,19,13,6]

    # Set up GPIO pins as inputs
    GPIO.setup(buttons, GPIO.IN)
    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        if channel == 6:
            global button_classify
            button_classify = True

    for button in buttons:
        GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

# Create a thread for button detection
button_thread = threading.Thread(target=gpio_init, daemon=True)
button_thread.start()

# Keep the program running indefinitely
try:
    gui.show_frame_1()
    while True:
        if button_classify:
            webcam.capture_and_crop_image()
            
            classification = model.classify()

            print('this is the max_label: ', classification)

            pill_info = tts.get_pill_info(classification)

            print(pill_info)

            # Uncomment the line below if you want to speak pill information in the button thread
            tts.speak_pill_info(pill_info)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting...')
except Exception as e:
    print('An error occurred:', e)
    GPIO.cleanup()

