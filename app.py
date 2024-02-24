import pyautogui as pg
import cv2
from hand_detector import HandDetector


cap = cv2.VideoCapture(0) # start the webcam
detector = HandDetector() # create hand detector object


while True:
    ret, frame = cap.read()

    detection_result = detector.detect_hands(frame)
    annotated_img = detector.draw_landmarks(frame, detection_result)  
    

    cv2.imshow('GestureCV', annotated_img)
    cv2.waitKey(1)