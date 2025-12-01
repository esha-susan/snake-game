import tkinter
import cv2
import threading
import time

import handtest as ht
import snake

#TUNING PARAMETERS
MOVE_THRESHOLD=50
TURN_DELAY=0.12

#GAME CONSTANTS
TILE=snake.TILE
WINDOW_WIDTH=snake.WINDOW_WIDTH
WINDOW_HEIGHT=snake.WINDOW_HEIGHT

#GLOBAL STATES FOR THREAD COMMUNICATION
vc=cv2.VideoCapture(0)
detector=ht.handDetector()
prev_x=None
prev_y=None
last_turn_time=time.time()

#INSTANCE OF THE GAME
game=snake.SnakeGame()

#SETTING UP TKINTER
window=tkinter.Tk()
window.title("Snake Xenzia")
window.resizable(False,False)
window.mainloop()
