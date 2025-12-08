# 🐍 Snake Xenzia — Hand Controlled (OpenCV + MediaPipe)

Control the classic Snake Xenzia game using only your hand gestures.
Your index finger becomes the joystick — move it in front of the webcam and the snake follows in real-time.

This project combines OpenCV, MediaPipe, and Tkinter to create a smooth, interactive, gesture-controlled gaming experience.

## Features


- Real-time hand tracking using MediaPipe

- Tracks landmark 8 (index fingertip) for direction control

- Smooth movement filtering (threshold + delay)

- Fully working Snake game with:

    - Food spawning

    - Collision detection

    - Score system

    - Growing snake body

- Live camera feed and game window run together

- Restart anytime with R

## Install Dependencies
pip install opencv-python mediapipe

## To run the project
python3 snakecontroller.py


## Controls

- Move index finger → Control snake direction

- R → Restart game

- Q or ESC (in camera window) → Quit

## System Workflow

- OpenCV captures frames from the webcam in real time

- MediaPipe Hands processes each frame and identifies 21 hand landmarks

- Landmark ID 8 (index fingertip) is extracted from the landmark array

- The fingertip’s X-coordinate maps to left/right movement and Y-coordinate to up/down

- A distance threshold ensures only intentional fingertip movements are detected

- Frame-to-frame smoothing reduces jitter and stabilizes the control input


