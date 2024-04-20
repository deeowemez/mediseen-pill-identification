#!/usr/bin/env python

#import libraries
import cv2
import os
import time
from edge_impulse_linux.image import ImageImpulseRunner

bbox_counter = 0
bbox_cycles = 2

# Initialize runner variable for ImageImpulseRunner class
runner = None

def now():
    #displays current time milliseconds
    return round(time.time() * 1000)

# def get_webcams():
#     '''
#         Establish connection to webcam associated with port 0
#     '''
#     port_ids = []
#     port = 0
#     camera = cv2.VideoCapture(port)
#     if camera.isOpened():
#         ret = camera.read()[0]
#         if ret:
#             backendName =camera.getBackendName()
#             w = camera.get(3)
#             h = camera.get(4)
#             print("Camera %s (%s x %s) found in port %s " %(backendName,h,w, port))
#             port_ids.append(port)
#         camera.release()
#     return port_ids
    
def get_bbox(res):
    ''' 
    Get the number of currently detected bounding boxes
    
    declares True for pill detection if frames show > 0 bounding boxes for three consecutive times
    '''
    global bbox_counter
    global bbox_cycles
    if "bounding_boxes" in res["result"].keys():
        if len(res["result"]["bounding_boxes"]) > 0:
            print('bbox before', bbox_counter)
            bbox_counter += 1
        if bbox_counter > 0 and len(res["result"]["bounding_boxes"]) == 0:
            bbox_counter = 0
            print('bbox reset', bbox_counter)
        if bbox_counter > bbox_cycles:
            bbox_counter = 0
            print('bbox reset', bbox_counter)
            return True
        else: return False

def detect_pill():
    '''
        Function for detecting the number of bounding boxes inside a frame taken by connected camera
    '''
    global bbox_counter
    
    # Path to model file
    model = "/home/pi/capstone/pill-identification/modelfile.eim"

    # Combines the directory path and model name 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    print('MODEL: ' + modelfile)

    with ImageImpulseRunner(modelfile) as runner:
        try:
            # Initializes the model 
            model_info = runner.init()
            print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
           
            # Opens a camera stream using the chosen port ID
            videoCaptureDeviceId = 0
            camera = cv2.VideoCapture(videoCaptureDeviceId)
            
            # Read a frame from the camera
            ret = camera.read()[0]
            
            # Establish connection to webcam associated with port 0
            if ret:
                backendName = camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                print("Camera %s (%s x %s) in port %s selected." % (backendName, h, w, videoCaptureDeviceId))
                camera.release()
            else:
                raise Exception("Couldn't initialize selected camera.")

            next_frame = 0  # limit to ~10 fps here
            
            # Loops through frames and classifications using the runner
            for res, img in runner.classifier(videoCaptureDeviceId):
                if (next_frame > now()):
                    time.sleep((next_frame - now()) / 1000)

                # Detects if pill is present in pill slot
                pill_detected = get_bbox(res)
                if pill_detected:
                    return True
                        
                # Updates next frame
                next_frame = now() + 100
                
        finally:
            if (runner):
                runner.stop()
                
if __name__ == "__main__":
    try:
        while True:
            detect_pill()
    except Exception as e:
        print(e)