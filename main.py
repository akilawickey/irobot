import cv2

# import imutils
import numpy as np
import RPi.GPIO as GPIO  
import time

cam = cv2.VideoCapture(0)

height = 240
width= 320


cam.set(3,width)
cam.set(4,height)

# GPIO Setup  

GPIO.setmode(GPIO.BCM)  
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #GPIO of Slave 


# Begin Loop  
try:
    while True:
      
        # frame = imutils.resize(frame, width=600)
        # frame =  cv2.bilateralFilter(frame,9,75,75)
        # cv2.imshow("test", frame)
        # if GPIO.input(23):
        if True:
            # cv2.imshow("test", frame)
        # k = cv2.waitKey(1)    
            ret, frame = cam.read()

            # frame = cv.QueryFrame(capture)
            
     

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # print hsv
            # show image
            blueLower = (90, 50, 50)
            blueUpper = (120, 255, 255)

            greenLower = (53, 74, 50)
            greenUpper = (80, 147, 255)

            redLower = (160, 100, 120)
            redUpper = (179, 255, 255)

            # blueLower = (100, 193, 191)
            # blueUpper = (105, 140, 61)

            # greenLower = (81, 247, 107)
            # greenUpper = (75, 204, 38)

            # redLower = (0, 168, 175)
            # redUpper = (2, 201, 73)

            # blueLower = (121, 255, 0)
            # blueUpper = (170, 0, 255)

            # greenLower = (61, 255, 0)
            # greenUpper = (120, 0, 255)

            # redLower = (0, 255, 0)
            # redUpper = (60, 0, 255)


            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)

            # cv2.imwrite('test123.png',blue_mask)
            # print blue_mask
            # mask = blue_mask + green_mask + red_mask
            red_count=0
            blue_count=0
            green_count=0

            for i in range(height):
                for j in range(width):
                    if red_mask[i][j]==255:
                        red_count+=1
                    if green_mask[i][j]==255:
                        green_count+=1
                    if blue_mask[i][j]==255:
                        blue_count+=1

            print
            print "red_count: " + str(red_count)
            print "greencount: " + str(green_count)
            print "blue count: " + str(blue_count)
            print


            if red_count>blue_count and red_count>green_count:
                print "red"
            elif blue_count > green_count:
                print "blue"
            elif green_count>0:
                print "green"
            else:
                print"cant identify"
            # if np.array_equal(mask, red_mask):
            #     print "Red Box"
            #     time.sleep(3)
                
            # elif np.array_equal(mask, green_mask):
            #     print "Green Box"
            #     time.sleep(3)
                
            # elif np.array_equal(mask, blue_mask):
            #     print "Blue Box" 
            #     time.sleep(3)
            for i in range(9):
                ret, frame = cam.read()
            

    for i in range(10):
        ret, frame = cam.read()
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
