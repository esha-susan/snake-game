# handtest.py

import cv2
import mediapipe as mp
import time

class handDetector():
    """
    A class to detect and track hands using MediaPipe.
    """
    def __init__(self, mode=False, maxHands=1, detectionConf=0.5, trackConf=0.5):
        # We enforce maxHands=1 for a simpler controller
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mp_hands = mp.solutions.hands
        # Correctly initialize the Hands object using keyword arguments
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConf,
            min_tracking_confidence=self.trackConf
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, frame, draw=True):
        """Processes the frame for hand detection."""
        # Flip the frame for a mirror-like view
        frame = cv2.flip(frame, 1)
        
        imgRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRgb)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame, handLms,
                        self.mp_hands.HAND_CONNECTIONS
                    )
        return frame

    def findPosition(self, frame, handNo=0, draw=True):
        """Finds the position of all landmarks on a detected hand."""
        lmList = []

        if self.results and self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

                # Optional drawing for landmark 8 (Index Finger Tip)
                if draw and id == 8:
                    cv2.circle(frame, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, "CONTROL", (cx - 40, cy - 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        return lmList

# Make sure this file is saved as handtest.py