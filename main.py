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
# from pydub import AudioSegment
# from pydub.playback import _play_with_simpleaudio
import pygame.mixer

# # Database connection information
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"
# mp3_folder = "/home/pi/capstone/pill-identification/mp3"
wav_folder = '/home/pi/capstone/pill-identification/wav'

# # Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# # Import libraries for gui
from tkinter import Tk
import tkinter as tk
import gui
import db
import ttkbootstrap as tb
from functools import partial

# Import libraries for accessing GPIO pins
import RPi.GPIO as GPIO
import threading

# # Import libraries for taking pictures
import webcam

# Import libraries for taking config
import sys, os, signal
import atexit
import datetime

set_frequency = 25000

# Initialize audio processing library
pygame.mixer.pre_init(frequency=set_frequency, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
print('channel: ', channel.get_busy())

def now():
    return datetime.datetime.now()

# initialzing GPIO
def gpio_init():
    GPIO.setmode(GPIO.BCM)

    buttons = [26,19,13] 
    # Set up GPIO pins as inputs
    GPIO.setup(buttons, GPIO.IN)
    
    GPIO.setup(22, GPIO.OUT)

    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        if channel == 26:
            tts.increase_volume()

        if channel == 19:
            tts.decrease_volume()
            
        if channel == 13:
            abort_audio()
            
    
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.RISING, callback=button_pressed, bouncetime=200)
    

def simulate_button_press():
    print('Simulating button press')
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.1)  # Adjust the duration as needed
    GPIO.output(22, GPIO.LOW)

def set_pill_run_classify():
    global pill_sensor
    print('set_pill_run_classify called')
    pill_sensor = True
    print('pill sensor: ', pill_sensor)
    if channel.get_busy():
        channel.stop()

def abort_audio():
    global classify_thread, pill_sensor
    pill_sensor = True
    # Abort the audio playback process if it's running
    if channel.get_busy():
        channel.stop()
        # Start the classify thread
        # classify(root)
        # classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
        # classify_thread.start()

classification = ''
identification_number = 0
pill_sensor = False

def repeat_pill_info_audio():
    global classification, channel
    if channel.get_busy():
        channel.stop()
        print('current: ', classification)
    tts.speak_pill_info(classification, channel)

def classify(root):
    global classification, identification_number, pill_sensor
    if not channel.get_busy():
        # print('identification number: ', identification_number)
        # time.sleep(1)
        if identification_number > 0:
            print('pill sensor: ', pill_sensor)
            # print('repeat:', repeat_button)
            if not pill_sensor:
                # show instructions frame after the last word of the previous audio if push button is not triggered during the previous classification audio output
                gui.show_instructions_frame(root)
                root.update()
            elif pill_sensor:
                # show image capture frame if push button is triggered during the audio output of a current classification
                gui.show_image_capture_frame(root)
                root.update()
                # repeat_button = False
        classification = model.classify()
        print('classification: ', classification)
        if classification == 'waiting for pill':
            gui.show_error_frame(root)
            root.update()
            tts.speak_error_audio()
            classify(root)
        elif classification:
            identification_number += 1
            pill_info = db.get_pill_info_gui(classification)
            gui.switch_pill_information_frame(root, 0, pill_info)
            root.update()
            pill_sensor = tts.speak_pill_info(classification, channel)
            # pill_sensor = False
            classification = ''
    # Schedule this function to run again after a certain time
    root.after(300, lambda: classify(root))  # Adjust the time interval as needed

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # root = tb.Window(themename='cosmo')
        # root.geometry('800x480')
        # root.title('')
        # root.iconbitmap('/home/pi/capstone/pill-identification/image.jpg')
        
        # Initialize the Tkinter root window
        root = tk.Tk()
        root.title('MediSeen')
        root.geometry("800x480")

        # Create a thread for button detection
        button_thread = threading.Thread(target=gpio_init, daemon=True)
        button_thread.start()

        # Show the logo frame
        gui.switch_frames(root, gui.show_logo_frame, 0)
        root.update()
        tts.speak_introductory_audio()

        # After 3 seconds, show the pill information frame
        gui.switch_frames(root, gui.show_instructions_frame, 200)
        
        # Create a thread for classifying medicines
        classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
        classify_thread.start()
                
        # Start the Tkinter event loop
        root.mainloop()

    except KeyboardInterrupt:
        print('Exiting...')
        GPIO.cleanup()
    except Exception as e:
        print('An error occurred:', e)
        GPIO.cleanup()
