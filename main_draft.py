#!/usr/bin/env python

# Import libraries for running model
import model
import time
import pill_detection

# # # Import libraries for tts
import tts
import sounddevice as sd
import numpy as np
import librosa
import alsaaudio

# # Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"

# # Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# # Function for initialzing GPIO
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

classification = ''
check_classification = False

# # Import libraries for gui
from tkinter import Tk
import tkinter as tk
import gui

# Import libraries for accessing GPIO pins
# import buttons
import RPi.GPIO as GPIO
import threading

# # Import libraries for taking pictures
import webcam

def check_classification(root):
    global classification
    global check_classification
    if classification != '':
        # Do something with the classification, e.g., switch to the pill information frame
        gui.switch_frames(root, gui.show_pill_information_frame, 0)
        # check_classification = True
    # Schedule this function to run again after a certain time
    root.after(1500, lambda: check_classification(root))  # Adjust the time interval as needed

def show_ins_frame(root):
    gui.switch_frames(root, gui.show_pill_information_frame, 0)

def gui_init():
    global classification
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.geometry("800x440")

    # Show the logo frame
    gui.switch_frames(root, gui.show_logo_frame, 0)

    # After 3 seconds, show the pill information frame
    gui.switch_frames(root, gui.show_instructions_frame, 1500)
    # root.after(0, lambda: show_ins_frame(root))

    # Start checking for classification
    root.after(1500, lambda: check_classification(root))

    # Start the Tkinter event loop
    root.mainloop()

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # Create a thread for GUI
        gui_thread = threading.Thread(target=gui_init)
        gui_thread.start() 
        
        # Create a thread for button detection
            # button_thread = threading.Thread(target=gpio_init, daemon=True)
            # button_thread.start()
        while True:     
            # classification = model.classify()
            time.sleep(7)
            classification = 'asdlkfjaklfs'
            print('classification_main: ', classification)
            if check_classification:
                print('inside check class')
                # tts.speak_pill_info(classification)
                # classification = ''
            time.sleep(5)

    except KeyboardInterrupt:
        # GPIO.cleanup()
        print('Exiting...')
    except Exception as e:
        print('An error occurred:', e)
        # GPIO.cleanup()
