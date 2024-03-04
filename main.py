# Shebang line
#!/usr/bin/env python

# import libraries
import model_draft
import tts_db

import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

import sqlite3
import pyttsx3

# Database connection information
pill_database = "pill_info.db"
pill_table = "pill_info_table"

runner = None
# Camera preview
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False
    
signal.signal(signal.SIGINT, model_draft.sigint_handler)


res = model_draft.inference(sys.argv[1:])

print('this is the max_label: ', max_label)