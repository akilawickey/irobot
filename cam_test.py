import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)
height = 240
width= 320


cap.set(3,width)
cap.set(4,height)

# Loop to continuously get images
while(1):
    # Read the frames frome a camera
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueLower = (90, 50, 50)
    blueUpper = (120, 255, 255)

    greenLower = (53, 74, 50)
    greenUpper = (80, 147, 255)

    redLower = (160, 100, 120)
    redUpper = (179, 255, 255)

    blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
    green_mask = cv2.inRange(hsv, greenLower, greenUpper)
    red_mask = cv2.inRange(hsv, redLower, redUpper)
    cv2.line(green_mask,(160,0),(160,240),(255,0,0),2)
    # show image
    cv2.imshow('frame', hsv)

    # if key pressed is 'Esc' then exit the loop
    if cv2.waitKey(33)== 27:
        break
    
# Clean up and exit the program
cv2.destroyAllWindows()
cap.release()
