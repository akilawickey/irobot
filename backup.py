import cv2
import imutils
import numpy as np
import RPi.GPIO as GPIO  
import time

cam = cv2.VideoCapture(1)

# GPIO Setup  

GPIO.setmode(GPIO.BCM)  
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #GPIO of Slave 


# Begin Loop  
try:
    while True:
        ret, frame = cam.read()

        # frame = imutils.resize(frame, width=600)
        frame =  cv2.bilateralFilter(frame,9,75,75)
        # cv2.imshow("test", frame)
        if GPIO.input(23):
            # cv2.imshow("test", frame)
        # k = cv2.waitKey(1)    
        
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # show image
            blueLower = (75, 109, 50)
            blueUpper = (130, 255, 255)

            greenLower = (50, 109, 20)
            greenUpper = (70, 255, 255)

            redLower = (160, 50, 120)
            redUpper = (179, 255, 255)

            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)
            # cv2.imwrite('test123.png',red_mask)
            mask = blue_mask + green_mask + red_mask

            if np.array_equal(mask, red_mask):
                print "Red Box"
            elif np.array_equal(mask, green_mask):
                print "Green Box"
            elif np.array_equal(mask, blue_mask):
                print "Blue Box" 


    # mask = cv2.inRange(hsv, blueLower, blueUpper)
    # print mask

        # blue_mask = cv2.erode(blue_mask, None, iterations=2)
        # blue_mask = cv2.dilate(blue_mask, None, iterations=2)   
 

        # image, contours, hier = cv2.findContours(blue_mask, cv2.RETR_TREE,
        #             cv2.CHAIN_APPROX_SIMPLE)
        # print contours

    # for c in contours:
    #   # get the bounding rect
    #   x, y, w, h = cv2.boundingRect(c)
    #   # draw a green rectangle to visualize the bounding rect
    #   cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #   # get the min area rect
    #   rect = cv2.minAreaRect(c)
    #   box = cv2.boxPoints(rect)
    #   # convert all coordinates floating point values to int
    #   box = np.int0(box)
    #   # draw a red 'nghien' rectangle
    #   cv2.drawContours(frame, [box], 0, (0, 0, 255))
    #   print 'Blue box detected'
    # time.sleep(3)
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt    
    GPIO.cleanup() # resets all GPIO ports used by this program
