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
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
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

# Initialize audio processing library
pygame.mixer.pre_init(frequency=25000, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.init()
channel = pygame.mixer.Channel(0)
print('channel: ', channel.get_busy())

audio_process = False

def speak_pill_info(classification):
    tempo = 1.4
    wav_classification = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
    wav_path = os.path.join(wav_folder, f"{wav_classification}.wav")
    print('wav_path: ', wav_path)
    audio_path = pygame.mixer.Sound(wav_path)
    channel.play(audio_path)
    print('channel: ', channel.get_busy())
    # channel.play(sound)
    # pygame.mixer.music.load(wav_path)
    # pygame.mixer.music.play()



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
            
        if channel == 13:
            # os.kill(os.getpid(), signal.SIGTERM)
            abort_audio_and_run_classify()
    
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=200)

def abort_audio_and_run_classify():
    global audio_process, classify_thread
    # Abort the audio playback process if it's running
    # wav_audio = classification.replace(' ', '_').replace('(', '').replace(')', '').lower()
    if channel.get_busy():
        # audio_process = False
        channel.stop()

    # Start the classify thread
    classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
    classify_thread.start()

classification = ''

def classify(root):
    global classification
    global audio_process
    classification = model.classify()
    if classification != '' and channel.get_busy() == False:
        pill_info = db.get_pill_info_gui(classification)
        gui.switch_pill_information_frame(root, 0, pill_info)
        root.update()
        audio_process = True
        print('audio:', audio_process)
        speak_pill_info(classification)
        audio_process = False
        classification = ''
    # Schedule this function to run again after a certain time
    root.after(0, lambda: classify(root))  # Adjust the time interval as needed

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # Create a thread for button detection
        button_thread = threading.Thread(target=gpio_init, daemon=True)
        button_thread.start()
        

        # root = tb.Window(themename='cosmo')
        # root.geometry('800x480')
        # root.title('')
        # root.iconbitmap('/home/pi/capstone/pill-identification/image.jpg')
        
        # Initialize the Tkinter root window
        root = tk.Tk()
        root.title('MediSeen')
        root.geometry("800x480")

        # Show the logo frame
        gui.switch_frames(root, gui.show_logo_frame, 0)
        root.update()
        # tts.speak_introductory_audio()

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
