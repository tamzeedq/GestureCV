import pyautogui as pg
import numpy as np
import math

class Mouse:
    def __init__(self, duration=0.3, cam_dim=(640, 480), screen_dim=(1920, 1080)):
        """
        Mouse object to handle mouse movement and events.

        Args:
            duration (float, optional): Duration to complete a mouse move. Defaults to 0.5.
            cam_dim (tuple[int], optional): Dimemsions of camera. Defaults to (640, 480).
            screen_dim (tuple[int], optional): Dimensions of monitor. Defaults to (1920, 1080).
        """
        self.duration = duration
        self.cam_w, self.cam_h = cam_dim
        self.screen_w, self.screen_h = screen_dim
        self.prev_mx, self.prev_my = pg.position()

    def move(self, detection_result):
        """
        Moves mouse to index fingeer detection coords. 
        Assumes detection_result.multi_hand_landmarks is not empty.

        Args:
            detection_result: MediaPipe Hand detection result.
        """
        
        hand = detection_result.multi_hand_landmarks[0]
        lm = hand.landmark[8] # index finger tip
        lmx, lmy = lm.x, lm.y
        
        # interpolate the position of the finger tip from webcam to the screen
        x = int(np.interp(lmx*self.cam_w, [0, self.cam_w], [0, self.screen_w]))
        y = int(np.interp(lmy*self.cam_h, [0, self.cam_h], [0, self.screen_h]))
        
        pg.moveTo(self.screen_w - x, y, self.duration, pg.easeOutQuad)
    
    
    def click(self, detection_result):
        """
        Simulates a left click if the index finger and the thumb are close to each other/pressed together.
        Assumes detection_result.multi_hand_landmarks is not empty.
        
        Args:
            detection_result: MediaPipe Hand detection result.
        """
        
        # Get euclidean distance between index finger and thumb
        hand = detection_result.multi_hand_landmarks[0]
        index_finger_tip = hand.landmark[8]
        thumb_tip = hand.landmark[4]
        
        dist = math.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
        # print(dist)
        if dist < 0.018: # arbitrary threshold, tune as needed
            pg.click()