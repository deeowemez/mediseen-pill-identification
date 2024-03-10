#!/usr/bin/env python

# import libraries for running model
import model_draft
import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

# import libraries for tts
import tts
import sqlite3
import pyttsx3

# import libraries for gui
import gui

# import libraries for accessing GPIO pins
import buttons
import RPi.GPIO as GPIO
import threading

# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

# Listens for Keyboard Interrupts
#signal.signal(signal.SIGINT, model_draft.sigint_handler)

def button_thread():
    try:
        buttons.gpio_init()
        while True:
            # Do other button-related stuff here...
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Exiting button thread...')
    except Exception as e:
        print('An error occurred in the button thread:', e)
        GPIO.cleanup()

# Create a thread for button detection
button_thread = threading.Thread(target=button_thread, daemon=True)
button_thread.start()

try:
    gui.show_frame_1()

    classification = model_draft.classify(sys.argv[1:])

    print('this is the max_label: ', classification)

    pill_info = tts.get_pill_info(classification)

    print(pill_info)

    #tts.speak_pill_info(pill_info)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exiting main script...')
except Exception as e:
    print('An error occurred in the main script:', e)
    GPIO.cleanup()