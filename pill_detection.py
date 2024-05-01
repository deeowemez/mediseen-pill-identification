#!/usr/bin/env python

#import libraries
import cv2
import os
import time
from edge_impulse_linux.image import ImageImpulseRunner

bbox_counter = 0
bbox_cycles = 0
bb_max_value = 0
pill_list = []
bb_dict = {}
bb_list = []
results_list = []

# Initialize runner variable for ImageImpulseRunner class
runner = None

def now():
    #displays current time milliseconds
    return round(time.time() * 1000)

def add_to_first_dict(res):
    # add to bounding box dictionary frame classifications
    global bb_dict, add_to_dict
    
    add_to_dict = {bb['label']: float(bb['value']) for bb in res['result']['bounding_boxes']}  
    
    for label, value in add_to_dict.items():
        if label in bb_dict and value > bb_dict[label]:
            # Update the value only if it's higher than the existing value
            bb_dict[label] = value
        elif label not in bb_dict:
            # If label doesn't exist, add it to the dictionary
            bb_dict[label] = value
    add_to_dict = {}

def max_in_dict():
    global bb_dict, bb_list, bb_max_value, results_list
    bb_list = list(bb_dict.values())
    for value in bb_list: 
        if value > bb_max_value: bb_max_value = value
    if len(bb_dict) > 0:
        # bb_max_label = bb_dict[]
        # bb_max_label = [label for label, value in bb_dict.items()][0]
        for label, value in bb_dict.items():
            if value == bb_max_value: 
                bb_max_label = label
                bb_final_max_value = value
        #     if value < 0: 
        #         bb_max_value_prediction = value
        bb_list.insert(0, bb_max_label)
        bb_list.insert(1, bb_final_max_value)
            
    # else: max_label = pill_detected[0]
    print('bb_list: ', bb_list)
    return bb_list

def get_bbox(res):
    ''' 
    Get the number of currently detected bounding boxes
    
    declares True for pill detection if frames show > 0 bounding boxes for three consecutive times
    '''
    global bbox_counter
    global bbox_cycles
    global pill_list
    global bb_list
    if "bounding_boxes" in res["result"].keys():
        if len(res["result"]["bounding_boxes"]) > 0:
            print('bbox before', bbox_counter)
            bbox_counter += 1
            add_to_first_dict(res)
            print('bb_dict: ', bb_dict)
        if bbox_counter > 0 and len(res["result"]["bounding_boxes"]) == 0:
            bbox_counter = 0
            print('bbox reset', bbox_counter)
        if bbox_counter > bbox_cycles:
            bbox_counter = 0
            print('bbox reset', bbox_counter)
            pill_list = max_in_dict()
            # for bb in res['result']['bounding_boxes']:
            #     pill_list.append(bb['label'])
            #     pill_list.append(bb['value'])
            #     print('in pill_detection: ', pill_list)
                # print('bb label: {} | bb value: {}' .format(bb['label'], bb['value']))
            return pill_list
        else: return False

def detect_pill():
    '''
        Function for detecting the number of bounding boxes inside a frame taken by connected camera
    '''
    global bbox_counter, bb_list
    
    # Path to model file
    model = "/home/pi/capstone/pill-identification/old_modelfile.eim"

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
                    return pill_detected
                        
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