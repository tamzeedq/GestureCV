import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        Initializes a MediaPipe Hand object.

        Args:
            static_image_mode (bool, optional): Defaults to False.
            max_num_hands (int, optional): Defaults to 1.
            min_detection_confidence (float, optional): Defaults to 0.5.
            min_tracking_confidence (float, optional): Defaults to 0.5.
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode, 
                                          max_num_hands=max_num_hands,
                                          min_detection_confidence=min_detection_confidence,
                                          min_tracking_confidence=min_tracking_confidence)
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_hands(self, image):
        """ 
        Run hand detection on the input image.

        Args:
            image: Image from cv2 camera

        Returns:
            NamedTuple: results from hand detection model
        """
        # Convert the BGR image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Get the hand landmarks
        results = self.hands.process(image_rgb)
        
        return results

    def draw_landmarks(self, image, results):
        """
        Draw landmarks on the input image and return the image.
        
        """
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
        return image
