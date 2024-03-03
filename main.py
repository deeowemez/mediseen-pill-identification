# Shebang line
#!/usr/bin/env python

# import libraries
import modelfile
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
    
signal.signal(signal.SIGINT, modelfile.sigint_handler)

modelfile.main(sys.argv[1:])

