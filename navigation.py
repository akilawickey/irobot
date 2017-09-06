import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)
height = 240
width= 320


cap.set(3,width)
cap.set(4,height)

# Loop to continuously get images
# while(1):
for i in range(1,10):
    # Read the frames frome a camera
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueLower = (100, 50, 50)
    blueUpper = (120, 255, 255)

    greenLower = (53, 74, 50)
    greenUpper = (90, 147, 255)

    redLower = (160, 100, 120)
    redUpper = (179, 255, 255)

    blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
    green_mask = cv2.inRange(hsv, greenLower, greenUpper)
    red_mask = cv2.inRange(hsv, redLower, redUpper)
    # cv2.line(green_mask,(160,0),(160,240),(255,0,0),2)
    # show image
    l_red_count=0
    l_blue_count=0
    l_green_count=0

    r_red_count=0
    r_blue_count=0
    r_green_count=0



    for i in range(height):
        for j in range(width/2):
            # if red_mask[i][j]==255:
            #     l_red_count+=1
            if green_mask[i][j]==255:
                l_green_count+=1
            if green_mask[i][j+width/2]==255:
                r_green_count+=1           
            # if blue_mask[i][j]==255:
            #     l_blue_count+=1

    print
    # print "left red_count: " + str(l_red_count)
    print "left greencount: " + str(l_green_count)
    # print "left blue count: " + str(l_blue_count)
    print

    print
    # print "Right red_count: " + str(r_red_count)
    print "Right greencount: " + str(r_green_count)
    # print "Right blue count: " + str(r_blue_count)
    print

    cv2.imshow('frame', green_mask)

    # if key pressed is 'Esc' then exit the loop
    if cv2.waitKey(33)== 27:
        break
    
# Clean up and exit the program
cv2.destroyAllWindows()
cap.release()
