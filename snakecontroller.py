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

canvas=tkinter.Canvas(
    window,bg="black",
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    borderwidth=0,
    highlightthickness=0
)
canvas.pack()
window.update()


#WINDOW PLACEMENT AT CENTER
window_x=int((window.winfo_screenwidth()/2)-window.winfo_width()/2)
window_y=int((window.winfo_screenheight()/2)-window.winfo_height()/2)
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{window_x}+{window_y}")


#RESETTING  THE GAME
def restart(event):
    global prev_x,prev_y,last_turn_time
    game.reset()
    prev_x,prev_y=None,None
    last_turn_time=time.time()
window.bind("r",restart)
window.bind("R",restart)

def run_camera_and_control():
    global prev_x,prev_y,last_trun_time
    T=snake.TILE
    while True:
        if not vc.isOpened():
            break
        rval,frame=vc.read()
        if not rval:
            continue
        
        frame=detector.findHands(frame,draw=True)
        lmList=detector.findPosition(frame,draw=False)

        if len(lmList)>8 and not game.gameover:
            x_f,y_f=lmList[8][1],lmList[8][2]


            if prev_x is not None and prev_y is not None:
                dx=x_f-prev_x
                dy=y_f-prev_y

                if time.time()-last_turn_time >TURN_DELAY:
                    new_vx,new_vy=game.velocityX,game.velocityY
                    turn_registered=False

                    if abs(dx)>abs(dy):
                        if dx>MOVE_THRESHOLD and game.velocityX!=-T:
                            new_vx,new_vy=T,0           #Right
                            turn_registered=True
                        elif dx < -MOVE_THRESHOLD and game.velocityX != T:
                            new_vx, new_vy = -T, 0     # Left
                            turn_registered = True
                        else:
                            if dy<-MOVE_THRESHOLD and game.velocityY!=T:
                                new_vx, new_vy = 0, -T     # Up 
                                turn_registered = True
                            elif dy > MOVE_THRESHOLD and game.velocityY != -T:
                                new_vx, new_vy = 0, T      # Down
                                turn_registered = True
                if turn_registered:
                    game.velocityX=new_vx
                    game.velocityY=new_vy
                    last_turn_time=time.time()
            
            prev_x,prev_y=x_f,y_f
        
        elif len(lmList)>8 and (prev_x is None and prev_y is None):
            prev_x,prev_y=x_f,y_f

        
    #VIDEO DISPLAY
        cv2.imshow("Snake Xenzia",frame)

        key=cv2.waitKey(1)
        if key==ord('q') or key==27:
                window.quit()
                break
vc.release()
cv2.destroyAllWindows()
