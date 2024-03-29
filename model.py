#!/usr/bin/env python

# import device_patches       # Device specific patches for Jetson Nano (needs to be before importing cv2)

import main
import cv2
import os
import sys, getopt
import numpy as np
import pill_detection
import webcam
import time
from edge_impulse_linux.image import ImageImpulseRunner

runner = None

bbox_dict = {}
max_label = ''
image_taken = 0
number_of_images = 0

def add_to_bbox_dict(res):
    # add to bounding box dictionary frame classifications
    global bbox_dict
    # print('len_dict before ', len(bbox_dict))
    add_to_dict = {bb['label']: float(bb['value']) for bb in res['result']['bounding_boxes']}  
    for label, value in add_to_dict.items():
        if label in bbox_dict and value > bbox_dict[label]:
            # Update the value only if it's higher than the existing value
            bbox_dict[label] = value
        elif label not in bbox_dict:
            # If label doesn't exist, add it to the dictionary
            bbox_dict[label] = value
    
    # print('len_dict after: ', len(bbox_dict))
    # print('bbox_dict: ', bbox_dict)

def max():
    # isolate classification with highest confidence
    global bbox_dict
    global max_label
    bbox_list = list(bbox_dict.values())
    for value in bbox_list: 
        max_value = 0
        if max_value is None or value > max_value: max_value = value
    if len(bbox_dict) > 0:
        max_label = [label for label, value in bbox_dict.items()][0]
    else: max_label = 'waiting for pill'
    return max_label

def classify():
    global number_of_images
    # Path to model file
    model = "/home/pi/capstone/pill-identification/modelfile.eim"

    # Combines the directory path and model name 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)
    
    print('MODEL: ' + modelfile)
    
    with ImageImpulseRunner(modelfile) as runner:
        try:        
            while True:
                global bbox_dict
                global max_label
                global image_taken
                # initialize runner
                runner.init()

                if pill_detection.detect_pill():
                    webcam.capture_and_crop_image()
                    img = cv2.imread('/home/pi/capstone/pill-identification/image.jpg')
                    image_taken += 1
                    if img is None:
                        print('Failed to load image', '/home/pi/capstone/pill-identification/image.jpg')
                        exit(1)

                    # imread returns images in BGR format, so we need to convert to RGB
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    # get_features_from_image also takes a crop direction arguments in case you don't have square images
                    features, cropped = runner.get_features_from_image(img)

                    # use runner object classify function to classify image features
                    res = runner.classify(features)
                    
                    # print('res', res)
                    
                    # add classification to bounding box dictionary
                    add_to_bbox_dict(res)
                    
                    #print('NUMBER: ', len(bbox_dict))
                    
                    if image_taken > number_of_images:
                        #save a copy of the picture as debug.jpg
                        number_of_images = 0
                        cv2.imwrite('debug.jpg', cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
                        print(bbox_dict)
                        max()
                        bbox_dict = {}
                        return max_label
                
        finally:
            if (runner):
                runner.stop()
            

            # if "classification" in res["result"].keys():
            #     print('Result (%d ms.) ' % (res['timing']['dsp'] + res['timing']['classification']), end='')
            #     for label in labels:
            #         score = res['result']['classification'][label]
            #         print('%s: %.2f\t' % (label, score), end='')
            #     print('', flush=True)

            # elif "bounding_boxes" in res["result"].keys():
            #     print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
            #     for bb in res["result"]["bounding_boxes"]:
            #         print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
            #         cropped = cv2.rectangle(cropped, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
            #         max_label = bb['label']

            # the image will be resized and cropped, save a copy of the picture here
            # so you can see what's being passed into the classifier
            # cv2.imwrite('debug.jpg', cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
            
if __name__ == "__main__":
    max_label_identification = classify()
    print('maxlabel:', max_label_identification)