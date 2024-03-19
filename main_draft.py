#!/usr/bin/env python

# Import libraries for running model
# import model
import time
# import pill_detection

# # Import libraries for tts
# import tts
# import sounddevice as sd
# import numpy as np
# import librosa
# import alsaaudio

# # Database connection information
# pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
# pill_table = "pill_info_table"

# # Initialize ALSA mixer
# mixer = alsaaudio.Mixer()

# # Function for initialzing GPIO
# def gpio_init():
#     GPIO.setmode(GPIO.BCM)

#     buttons = [26,19,13,6]

#     # Set up GPIO pins as inputs
#     GPIO.setup(buttons, GPIO.IN)
    
#     def button_pressed(channel):
#         print(f"Button is pressed on channel {channel}")
        
#         if channel == 26:
#             tts.increase_volume()

#         if channel == 19:
#             tts.decrease_volume()
    
#     for button in buttons:
#         GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

classification = ''
check_classification = False

# # Import libraries for gui
from tkinter import Tk
import tkinter as tk
import gui

# # Import libraries for accessing GPIO pins
# # import buttons
# import RPi.GPIO as GPIO
import threading

# # Import libraries for taking pictures
# import webcam

def gui_init():
    global classification
    global check_classification
    # Initialize the Tkinter root window
    root = tk.Tk()
    root.geometry("800x480")

    # Show the logo frame
    root.after(0, lambda: gui.switch_frame(root, gui.show_logo_frame))

    # After 3 seconds, show the pill information frame
    gui.switch_frames(root, gui.show_instructions_frame, 1500)

    if classification:
        gui.check_and_show_pill_information(root, 2000, classification)
        check_classification = True

    # Start the Tkinter event loop
    root.mainloop()

# def check_and_show_pill_information(root, classification):
#     if classification:
#         gui.switch_frames(root, gui.show_pill_information_frame, 0)

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # while True:     
        # Create a thread for button detection
        # button_thread = threading.Thread(target=gpio_init, daemon=True)
        # button_thread.start()

        # Create a thread for GUI
        gui_thread = threading.Thread(target=gui_init)
        gui_thread.start() 
            
        classification = model.classify()
        print('classification_main: ', classification)
        if check_classification:
            print('inside check class')
            # tts.speak_pill_info(classification)      
        
        # # Start periodic check for classification
        # classification = 'Glucophage XR Metformin HCl 750mg (Unpacked)'
        # if classification:
        #     print('laskdjf')
        #     root.after(3000, root.destroy)  # Close the window after 3000 milliseconds (3 seconds)
        #     gui.show_logo_frame(root)
        # else:
        #     print('asdf')
        #     root.after(3000, root.destroy)  # Close the window after 3000 milliseconds (3 seconds)
        #     gui.show_instructions_frame(root)
        #     # Schedule the next check after 1000 ms (1 second)
        #     root.after(1000, check_classification)

        # # Start the periodic classification check
        # check_classification()

    except KeyboardInterrupt:
        # GPIO.cleanup()
        print('Exiting...')
    except Exception as e:
        print('An error occurred:', e)
        # GPIO.cleanup()
