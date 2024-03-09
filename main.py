#!/usr/bin/env python

# # import libraries
# import model_draft
# import pills_gtts

# import cv2
# import os
# import sys, getopt
# import signal
# import time
# from edge_impulse_linux.image import ImageImpulseRunner

import gui
# import output.frame2.build.assets.frame0.frame_2 as frame_2
# import output.frame3.build.assets.frame0.frame_3 as frame_3
# import output.frame4.build.assets.frame0.frame_4 as frame_4

# import sqlite3
# import pyttsx3

# # Database connection information
# pill_database = "pill_info.db"
# pill_table = "pill_info_table"

# runner = None
# #Camera preview
# show_camera = True
# if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
#     show_camera = False
    
# signal.signal(signal.SIGINT, model_draft.sigint_handler)

# classification = model_draft.classify(sys.argv[1:])

# print('this is the max_label: ', classification)

# pill_info = pills_gtts.speak_pill_info(classification)

# pills_gtts.speak_pill_info(pill_info)

gui.show_frame_4()

