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

# Import libraries for config
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

rgb_init_event = threading.Event()
repeat_event = threading.Event()

global red_pwm
global green_pwm
global blue_pwm

def rgb_init():
    global red_pwm
    global green_pwm
    global blue_pwm

    GPIO.setmode(GPIO.BCM)
    
    # Define the pins for RGB LED
    red_pin = 22
    green_pin = 27
    blue_pin = 17
    
    # Set up PWM channels
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)
    
    red_pwm = GPIO.PWM(red_pin, 100)  # PWM frequency for red LED
    green_pwm = GPIO.PWM(green_pin, 100)  # PWM frequency for green LED
    blue_pwm = GPIO.PWM(blue_pin, 100)  # PWM frequency for blue LED

    red_pwm.start(0)  # Start PWM with 0% duty cycle
    green_pwm.start(0)
    blue_pwm.start(0) 
    
    # Set the event to indicate that initialization is complete
    rgb_init_event.set()

def set_color(red, green, blue):
    red_pwm.ChangeDutyCycle(red)
    green_pwm.ChangeDutyCycle(green)
    blue_pwm.ChangeDutyCycle(blue)

# initialzing GPIO
def gpio_init():
    GPIO.setmode(GPIO.BCM)

    # Define the pins for push buttons
    buttons = [26,19,13] 
    GPIO.setup(buttons, GPIO.IN)
    GPIO.setup(21, GPIO.OUT)
    
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

# Define a function to set the color of the RGB LED

def simulate_button_press():
    print('Simulating button press')
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.1)  # Adjust the duration as needed
    GPIO.output(21, GPIO.LOW)

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


classification = ''
identification_number = 0
pill_sensor = False

def repeat_pill_info_audio(current_pill):
    repeat_event.set()
    print('print: ', current_pill)
    if repeat_event.is_set():
        print('repeat_event.is_set')
    global channel 
    if channel.get_busy():
        # print(channel.get_sound())
        channel.stop()
    print('current: ', current_pill)
    tts.speak_pill_info(current_pill, channel)
    repeat_event.clear()

def classify(root):
    global classification, identification_number, pill_sensor, current_pill
    if repeat_event.is_set():
        print('repeat_event.is_set in classify')
    if not channel.get_busy() and not repeat_event.is_set():
        # print('identification number: ', identification_number)
        if identification_number > 0:
            print('pill sensor: ', pill_sensor)
            if not pill_sensor:
                # show instructions frame after the last word of the previous audio if push button is not triggered during the previous classification audio output
                gui.show_instructions_frame(root)
                root.update()
            elif pill_sensor:
                # show image capture frame if push button is triggered during the audio output of a current classification
                gui.show_image_capture_frame(root)
                root.update()
        set_color(60, 60, 93) # Set rgb led to cyan
        classification = model.classify()
        print('classification: ', classification)
        if classification == 'waiting for pill':
            set_color(90, 5, 8) # Set rgb led to red
            gui.show_error_frame(root)
            root.update()
            tts.speak_error_audio()
            pill_sensor = False
            # classify(root)
        elif classification:
            print('classification: ', classification)
            identification_number += 1
            set_color(45, 100, 20)  # Set rgb led to green
            pill_info = db.get_pill_info_gui(classification)
            gui.switch_pill_information_frame(root, 0, pill_info)
            root.update()
            pill_sensor = tts.speak_pill_info(classification, channel)
            # classification = ''
    # Schedule this function to run again after a certain time
    root.after(0, lambda: classify(root))  # Adjust the time interval as needed

# Keep the program running indefinitely

if __name__ == "__main__":
    # Keep the program running indefinitely
    try:
        # GPIO.cleanup()
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
        
        # Create a thread for controlling the RGB LED
        led_thread = threading.Thread(target=rgb_init, daemon=True) 
        led_thread.start()

        # Wait for the initialization to complete
        rgb_init_event.wait()
        
        set_color(100, 60, 10) # Set rgb led to yellow

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
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(0)
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print('An error occurred:', e)
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(0)
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()
