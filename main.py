#!/usr/bin/env python

# import libraries
import model_draft
import tts

import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

import gui

import sqlite3
import pyttsx3

# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

# gui.show_frame_1()

runner = None
#Camera preview
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False
    3
signal.signal(signal.SIGINT, model_draft.sigint_handler)

classification = model_draft.classify(sys.argv[1:])

print('this is the max_label: ', classification)

pill_info = tts.get_pill_info(classification)

tts.speak_pill_info(pill_info)
