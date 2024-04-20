#!/usr/bin/env python

# Import libraries for running model
import model
import time
import math

# Import libraries for tts
import tts
import alsaaudio
import pygame.mixer

# # Import libraries for gui
import tkinter as tk
import gui
import db

# Import libraries for accessing GPIO pins
import RPi.GPIO as GPIO
import threading

# Import libraries for config
import subprocess

# Folder path
pill_database = "/home/pi/capstone/pill-identification/database/pill_info.db"
pill_table = "pill_info_table"
wav_folder = '/home/pi/capstone/pill-identification/wav'

# Initialize audio processing library
set_frequency = 25000
pygame.mixer.pre_init(frequency=set_frequency, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.init()
channel = pygame.mixer.Channel(0)

# Initialize ALSA mixer
mixer = alsaaudio.Mixer()

# Initialize threading events
rgb_init_event = threading.Event()
repeat_event = threading.Event()
pill_info_finished_event = threading.Event()

# Initialize global variables
global red_pwm
global green_pwm
global blue_pwm
classification = ''
identification_number = 0
pill_sensor = False
reclassify_button = 23

def rgb_init():
    '''
        Initializes GPIO pins and PWM for RGB LED. Defines function for changing RGB color
    '''
    global red_pwm
    global green_pwm
    global blue_pwm

    GPIO.setmode(GPIO.BCM)
    
    # Define the pins for RGB LED
    red_pin = 27
    green_pin = 18
    blue_pin = 22
    
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


def gpio_init():
    '''
        Initialzes GPIO and defines callback functions for detection of a falling edge event for each push button
    '''
    GPIO.setmode(GPIO.BCM)
    
    # Define the pins for push buttons
    buttons = [21,26,16,13,24] 
    GPIO.setup(buttons, GPIO.IN)
    global reclassify_button
    GPIO.setup(reclassify_button, GPIO.OUT)
    
    def button_pressed(channel):
        print(f"Button is pressed on channel {channel}")
        
        if channel == 21:
            tts.increase_volume()

        if channel == 26:
            tts.decrease_volume()
            
        if channel == 16 or channel == 24:
            abort_audio()
            
        if channel == 13:
            shutdown()
        
    for button in buttons:
        GPIO.add_event_detect(button, GPIO.RISING, callback=button_pressed, bouncetime=200)

def simulate_button_press():
    '''
        Callback function for reclassify GUI button for simulating a button press at output pin 23 and input pin 24
    '''
    global reclassify_button
    print('Simulating button press')
    GPIO.output(reclassify_button, GPIO.HIGH)
    time.sleep(0.1) 
    GPIO.output(reclassify_button, GPIO.LOW)
    time.sleep(0.1)

def abort_audio():
    '''
        Stops audio playing in audio channel whenever reclassify push button or reclassify GUI button is triggered
    '''
    global classify_thread, pill_sensor
    pill_sensor = True
    print('pill sensor: ', pill_sensor)
    # Abort the audio playback process if it's running
    if channel.get_busy():
        channel.stop()
    
def shutdown():
    '''
        Callback function for shtudown push button
    '''
    print("Button pressed, shutting down...")
    # Close all open windows
    subprocess.run(["wmctrl", "-c", ":ALL:"])
    # Shutdown Raspberry Pi
    subprocess.run(["sudo", "shutdown", "-h", "now"])

def repeat_pill_info_audio(current_pill):
    '''
        Callback function for repeat pill info GUI button
    '''
    global channel 
    repeat_event.set()
    print('print: ', current_pill)
    if repeat_event.is_set():
        print('repeat_event.is_set')
    # Stop and repeat audio playback in audio channel
    if channel.get_busy():
        channel.stop()
    print('current: ', current_pill)
    tts.speak_pill_info(current_pill, channel)
    repeat_event.clear()

def wait_for_channel(channel, duration):
    # Force pygame to wait for a duration of time when channel is busy
    while channel.get_busy():
        pygame.time.wait(math.ceil(duration))

def classify(root):
    '''
        Main classify function that runs in loop
    '''
    global classification, identification_number, pill_sensor, pill_info
    # Skips block when channel is currently playing an audio file or when repeat event flag is set
    if not channel.get_busy() and not repeat_event.is_set():                                                                                                                                                                                                                                                                              
        if identification_number > 0:
            if not pill_sensor:
                # show instructions frame after the last word of the previous audio if push button is not triggered during the previous classification audio output
                gui.show_instructions_frame(root)
                root.update()
            elif pill_sensor:
                # show image capture frame if push button is triggered during the audio output of a current classification
                gui.show_image_capture_frame(root)
                root.update()
        set_color(60, 60, 95) # Set rgb led to cyan
        
        # Perform inference for pill classification
        classification = model.classify()
        print('classification: ', classification)
        
        # Perform display and audio output for pill classification error
        if classification == 'waiting for pill':
            set_color(95, 5, 5) # Set rgb led to red
            gui.show_error_frame(root)
            root.update()
            tts.speak_error_audio()
            pill_sensor = False
        
        # Perform display and audio output for corresponding pill classification
        elif classification:
            print('classification: ', classification)
            identification_number += 1
            set_color(50, 100, 20)  # Set rgb led to green
            
            # Show display output pill information frame 
            pill_info = db.get_pill_info_gui(classification)
            gui.switch_pill_information_frame(root, 0, pill_info)
            root.update()

            # Play pill information audio playback 
            pill_info_duration = tts.speak_pill_info(classification, channel)
            wait_for_channel(channel, (pill_info_duration))
            pill_sensor = False
            
            # Start the sequence of audio playback for rtc
            current_duration = tts.speak_rtc(channel)
            print('current duration: ', math.ceil(current_duration))
            wait_for_channel(channel, current_duration)
            hour_duration = tts.speak_hour(channel)
            wait_for_channel(channel, hour_duration)
            min_duration = tts.speak_min(channel)
            wait_for_channel(channel, min_duration)
            tts.speak_am_pm(channel)
            

    # Schedule this function to run again after a certain time
    root.after(0, lambda: classify(root))  


if __name__ == "__main__":
    try:        
        # Initialize the Tkinter root window
        root = tk.Tk()
        root.geometry("800x480")
        
        # Create a thread for controlling the RGB LED
        led_thread = threading.Thread(target=rgb_init, daemon=True) 
        led_thread.start()

        # Wait for the initialization to complete
        rgb_init_event.wait()
        
        set_color(100, 60, 10) # Set rgb led to yellow

        # Show the logo frame
        # gui.switch_frames(root, gui.show_logo_frame, 0)
        gui.show_logo_frame(root)
        root.update()
        tts.speak_introductory_audio()

        # After 3 seconds, show the pill information frame
        gui.switch_frames(root, gui.show_instructions_frame, 200)
        
        # Create a thread for button detection
        button_thread = threading.Thread(target=gpio_init, daemon=True)
        button_thread.start()
        
        # Create a thread for classifying medicines
        classify_thread = threading.Thread(target=classify, args=(root,), daemon=True)
        classify_thread.start()
                
        # Start the Tkinter event loop
        root.mainloop()

    except KeyboardInterrupt:
        print('Exiting...')
        GPIO.cleanup()
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print('An error occurred:', e)
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.cleanup()
