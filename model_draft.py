#!/usr/bin/env python

#import libraries
import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

# Initialize runner variable for ImageImpulseRunner class
runner = None
# Camera preview
show_camera = True
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

def max(res):
    # isolate classification with highest confidence
    bbox_dict = {bb['label']: float(bb['value']) for bb in res['result']['bounding_boxes']}  
    bbox_list = list(bbox_dict.values())
    for value in bbox_list: 
        max_value = 0
        if max_value is None or value > max_value: max_value = value
    max_label = [label for label, value in bbox_dict.items()][0]
    return max_label

def get_bbox(res):
    #pill_detected = False
    if "bounding_boxes" in res["result"].keys():
        if len(res["result"]["bounding_boxes"]) > 0:
            return True
        else: return False
    
def inference(argv):
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

                pill_detected = get_bbox(res)

                print('classification runner response', res)

                if pill_detected:
                
                    for bb in res['result']['bounding_boxes']:
                        print(bb['label'])
                    

                    if "bounding_boxes" in res["result"].keys():
                        # Print box coordinates and draws on image
                        print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                        for bb in res["result"]["bounding_boxes"]:
                            print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                            img = cv2.rectangle(img, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
                        print('Max Label: ', max(res))

                    if (show_camera):
                        # Displays image with boxes
                        cv2.imshow('edgeimpulse', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                        if cv2.waitKey(1) == ord('q'):
                            break
                    
                    # Updates next frame
                    next_frame = now() + 100
                
                else: print("Waiting for pill")
            
        finally:
            if (runner):
                runner.stop()
                
    return (res)

if __name__ == "__main__":
    inference(sys.argv[1:])