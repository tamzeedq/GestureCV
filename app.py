import pyautogui as pg
import cv2
from hand_detector import HandDetector
from mouse import Mouse
import numpy as np
import time


cap = cv2.VideoCapture(0) # start the webcam

# get dimensions of the webcam and the screen
cam_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
screen_w, screen_h = pg.size()

detector = HandDetector() # create hand detector object
mouse = Mouse(cam_dim=(cam_w, cam_h), screen_dim=(screen_w, screen_h)) # create mouse object


while True:
    ret, frame = cap.read()

    detection_result = detector.detect_hands(frame)
    annotated_img = detector.draw_landmarks(frame, detection_result)  
    
    # handle events
    if detection_result.multi_hand_landmarks:
        mouse.move(detection_result)
        
        # Check for a gesture
        if not detector.check_gesture(detection_result):
            mouse.click(detection_result) # simulate a click if the gesture is not detected
        
    cv2.imshow('GestureCV', annotated_img)
    cv2.waitKey(1)