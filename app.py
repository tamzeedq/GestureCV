import pyautogui as pg
import cv2
from hand_detector import HandDetector
import numpy as np
import time


SMTH_FACT = 0.3 # smoothening factor; 0 < x <= 1, the higher the value, the less smooth

cap = cv2.VideoCapture(0) # start the webcam
detector = HandDetector() # create hand detector object

# get dimensions of the webcam and the screen
cam_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
screen_w, screen_h = pg.size()

# initialize the previous mouse position
prev_mx, prev_my = pg.position()

while True:
    ret, frame = cap.read()

    detection_result = detector.detect_hands(frame)
    annotated_img = detector.draw_landmarks(frame, detection_result)  
    
    # handle mouse movement
    if detection_result.multi_hand_landmarks:
        hand = detection_result.multi_hand_landmarks[0]
        lm = hand.landmark[8] # index finger tip
        lmx, lmy = lm.x, lm.y
        
        # interpolate the position of the finger tip from webcam to the screen
        x = np.interp(lmx*cam_w, [0, cam_w], [0, screen_w])
        y = np.interp(lmy*cam_h, [0, cam_h], [0, screen_h])
        
        # smoothen the movement
        new_mx = prev_mx + (x - prev_mx) * SMTH_FACT
        new_my = prev_my + (y - prev_my) * SMTH_FACT
        
        pg.moveTo(screen_w - new_mx, new_my) # flip the x-axis to match the screen
        prev_mx, prev_my = new_mx, new_my
    
    cv2.imshow('GestureCV', annotated_img)
    cv2.waitKey(1)
    # time.sleep(0)    