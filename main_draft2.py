#!/usr/bin/env python

# Import libraries for running model
import model
import time

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

# # Import libraries for gui
from tkinter import Tk
import tkinter as tk
import gui
import db

# Import libraries for accessing GPIO pins
import RPi.GPIO as GPIO
import threading

# # Import libraries for taking pictures
import webcam

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

def classify(root):
    global classification
    classification = model.classify()
    if classification != '':
        pill_info = db.get_pill_info_gui(classification)
        gui.switch_pill_information_frame(root, 0, pill_info)
        root.update()
        tts.speak_pill_info(classification)
        classification = ''
    # Schedule this function to run again after a certain time
    root.after(100, lambda: classify(root))  # Adjust the time interval as needed

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # Create a thread for button detection
        button_thread = threading.Thread(target=gpio_init, daemon=True)
        button_thread.start()
        
        # Initialize the Tkinter root window
        root = tk.Tk()
        root.geometry("800x480")

        # Show the logo frame
        gui.switch_frames(root, gui.show_logo_frame, 0)
        root.update()
        tts.speak_introductory_audio()

        # After 3 seconds, show the pill information frame
        gui.switch_frames(root, gui.show_instructions_frame, 2000)
        
        # Create a thread for classifying medicines
        classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
        classify_thread.start()
        
        # root.after(0, lambda: check_classification(root))
        
        # Start the Tkinter event loop
        root.mainloop()

    except KeyboardInterrupt:
        print('Exiting...')
    except Exception as e:
        print('An error occurred:', e)
