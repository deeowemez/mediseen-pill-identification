#!/usr/bin/env python

#import libraries
import cv2
import os
import time
from edge_impulse_linux.image import ImageImpulseRunner

bbox_counter = 0
bbox_dict = {}
max_label = ''

# Initialize runner variable for ImageImpulseRunner class
runner = None

def now():
    #displays current time milliseconds
    return round(time.time() * 1000)

def get_webcams():
    # establish connection to webcam associated with port 0
    port_ids = []
    port = 0
    camera = cv2.VideoCapture(port)
    if camera.isOpened():
        ret = camera.read()[0]
        if ret:
            backendName =camera.getBackendName()
            w = camera.get(3)
            h = camera.get(4)
            print("Camera %s (%s x %s) found in port %s " %(backendName,h,w, port))
            port_ids.append(port)
        camera.release()
    return port_ids

# def add_to_bbox_dict(res):
#     # add to bounding box dictionary frame classifications
#     global bbox_dict
#     print('len_dict before ', len(bbox_dict))
#     add_to_dict = {bb['label']: float(bb['value']) for bb in res['result']['bounding_boxes']}  
#     for label, value in add_to_dict.items():
#         if label in bbox_dict and value > bbox_dict[label]:
#             # Update the value only if it's higher than the existing value
#             bbox_dict[label] = value
#         elif label not in bbox_dict:
#             # If label doesn't exist, add it to the dictionary
#             bbox_dict[label] = value
    
#     print('len_dict after: ', len(bbox_dict))
#     print('bbox_dict: ', bbox_dict)

# def max():
#     # isolate classification with highest confidence
#     global bbox_dict
#     bbox_list = list(bbox_dict.values())
#     for value in bbox_list: 
#         max_value = 0
#         if max_value is None or value > max_value: max_value = value
#     if len(bbox_dict) > 0:
#         max_label = [label for label, value in bbox_dict.items()][0]
#     else: max_label = 'waiting for pill'
#     return max_label

def increment_reset_bbox():
    global bbox_counter
    bbox_counter += 1
    
def get_bbox(res):
    global bbox_counter
    global bbox_dict
    if "bounding_boxes" in res["result"].keys():
        if len(res["result"]["bounding_boxes"]) > 0:
            print('bbox before', bbox_counter)
            increment_reset_bbox()
            # add_to_bbox_dict(res)
        if bbox_counter > 0 and len(res["result"]["bounding_boxes"]) == 0:
            bbox_counter = 0 
            bbox_dict = {}
            print('bbox reset', bbox_counter)
            print('bbox dict reset', bbox_dict)
        if bbox_counter > 2:
            print('bbox reset', bbox_counter)
            return True
        else: return False

def detect_pill():
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
            # Extracts labels used for prediction
            videoCaptureDeviceId = 0

            # Opens a camera stream using the chosen port ID
            camera = cv2.VideoCapture(videoCaptureDeviceId)
            # Read a frame from the camera
            ret = camera.read()[0]
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
        detect_pill()
    except Exception as e:
        print(e)