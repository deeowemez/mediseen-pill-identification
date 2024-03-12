#!/usr/bin/env python

#import libraries
import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

bbox_counter = 0
bbox_dict = {}
max_label = ''

# Initialize runner variable for ImageImpulseRunner class
runner = None
# Camera preview
show_camera = False
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False

def now():
    #displays current time milliseconds
    return round(time.time() * 1000)

def get_webcams():
    # searches for available webcams through port 1 - 4
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

def sigint_handler(sig, frame):
    # exits program with keyboard interrupt (ctrl + c)
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def help():
    # script for running model and what camera port to use
    print('python classify.py <path_to_model.eim> <Camera port ID, only required when more than 1 camera is present>')

def add_to_bbox_dict(res):
    # add to bounding box dictionary frame classifications
    global bbox_dict
    print('len_dict before ', len(bbox_dict))
    add_to_dict = {bb['label']: float(bb['value']) for bb in res['result']['bounding_boxes']}  
    
    for label, value in add_to_dict.items():
        if label in bbox_dict and value > bbox_dict[label]:
            # Update the value only if it's higher than the existing value
            bbox_dict[label] = value
        elif label not in bbox_dict:
            # If label doesn't exist, add it to the dictionary
            bbox_dict[label] = value
    
    print('len_dict after: ', len(bbox_dict))
    print('bbox_dict: ', bbox_dict)

def max():
    # isolate classification with highest confidence
    global bbox_dict
    bbox_list = list(bbox_dict.values())
    for value in bbox_list: 
        max_value = 0
        if max_value is None or value > max_value: max_value = value
    if len(bbox_dict) > 0:
        max_label = [label for label, value in bbox_dict.items()][0]
    else: max_label = 'waiting for pill'
    return max_label

def increment_reset_bbox():
    global bbox_counter
    bbox_counter += 1
    
def runner_stop():
    global bbox_counter
    global bbox_dict
    global max_label
    max_label = max()
    print('Max Label: ', max_label)
    bbox_counter = 0
    bbox_dict = {}

def get_bbox(res):
    global bbox_counter
    if "bounding_boxes" in res["result"].keys():
        if len(res["result"]["bounding_boxes"]) > 0:
            print('bbox before', bbox_counter)
            increment_reset_bbox()
            add_to_bbox_dict(res)
            print('bbox after', bbox_counter)
            if bbox_counter > 3:
                runner_stop()
                print('bbox reset', bbox_counter)
                return True
            else: return False

def classify(argv):
    global bbox_counter
    global max_label
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

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
            labels = model_info['model_parameters']['labels']
            #print('Labels: ', labels)
            # Determines webcam to be used
            if len(args) >= 2:
                videoCaptureDeviceId = int(args[1])
            else:
                port_ids = get_webcams()
                if len(port_ids) == 0:
                    raise Exception('Cannot find any webcams')
                if len(args) <= 1 and len(port_ids) > 1:
                    raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use this script")
                videoCaptureDeviceId = int(port_ids[0])

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

                #print('classification runner response', res)
                
                for bb in res['result']['bounding_boxes']:
                    print(bb['label'])
                
                img_resized = cv2.resize(img, (400, 400))
                
                if "bounding_boxes" in res["result"].keys():
                    # Print box coordinates and draws on image
                    print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                    for bb in res["result"]["bounding_boxes"]:
                        print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                        # img = cv2.rectangle(img, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
                        img_resized = cv2.rectangle(img_resized, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
                    #print('Max Label: ', max(res))
                    
                if (show_camera):
                    # Displays image with boxes
                    cv2.imshow('edgeimpulse', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                    if cv2.waitKey(1) == ord('q'):
                        break
                
                # Updates next frame
                next_frame = now() + 100
                
                # Detects if pill is present in pill slot
                pill_detected = get_bbox(res)
                if pill_detected:
                    return (max_label)
                        
        finally:
            if (runner):
                runner.stop()
                
if __name__ == "__main__":
    classify(sys.argv[1:])