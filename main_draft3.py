#!/usr/bin/env python

# Import libraries for running model
import model
import time
import pill_detection

# Import libraries for tts
import tts
import sounddevice as sd
import numpy as np
import librosa
import alsaaudio

# Import libraries for gui
import others.gui as gui

# Import libraries for accessing GPIO pins
# import buttons
import RPi.GPIO as GPIO
import threading

# Import libraries for taking pictures
import webcam

# Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"

# Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# Function for initialzing GPIO
def gpio_init():
    GPIO.setmode(GPIO.BCM)

    buttons = [26,19,13,6]

    # Set up GPIO pins as inputs
    GPIO.setup(buttons, GPIO.IN)
    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        if channel == 26:
            tts.increase_volume()

        if channel == 19:
            tts.decrease_volume()
    
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

# Create a thread for button detection
button_thread = threading.Thread(target=gpio_init, daemon=True)
button_thread.start()


# Function to switch GUI frames
def switch_frame(new_frame_function):
    global current_frame
    if current_frame:
        # Close the current frame
        current_frame.destroy()
        
    current_frame = new_frame_function()

# Create a thread for gui
gui_thread = threading.Thread(target=switch_frame, daemon=True)
gui_thread.start()

# Keep the program running indefinitely
try:
    current_frame = None
    while True:
        # classification = model.classify()
        
        classification = 'Glucophage XR Metformin HCl 750mg (Unpacked)'

        print('this is the max_label: ', classification)
        
        # switch_frame(gui.show_pill_information_frame)
        # time.sleep(3)  # Show the instructions frame for 5 seconds

        # Uncomment the line below if you want to speak pill information in the button thread
        #tts.speak_pill_info(classification)
        
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting...')
except Exception as e:
    print('An error occurred:', e)
    GPIO.cleanup()

