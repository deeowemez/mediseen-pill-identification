#!/usr/bin/env python

# Import libraries for running model
import model
import time

# Import libraries for tts
import tts

# Import libraries for gui
import gui

# Import libraries for accessing GPIO pins
import buttons
import RPi.GPIO as GPIO
import threading

# Import libraries for taking pictures
import webcam

# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

# Listens for Keyboard Interrupts
# signal.signal(signal.SIGINT, model_draft.sigint_handler)

def button_thread():
    try:
        buttons.gpio_init()
        #gui.show_frame_1()
        # while True:

        
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Exiting button thread...')
    except Exception as e:
        print('An error occurred in the button thread:', e)
        GPIO.cleanup()

# Create a thread for button detection
button_thread = threading.Thread(target=button_thread, daemon=True)
button_thread.start()

# Keep the program running indefinitely
try:
    while True:
        if buttons.classify():
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
