import cv2

# import imutils
import numpy as np
import RPi.GPIO as GPIO  
import time
import serial

cam = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyACM0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

height = 240
width= 320
blueLower = (100, 50, 50)
blueUpper = (120, 255, 255)

greenLower = (53, 74, 50)
greenUpper = (90, 147, 255)

redLower = (160, 100, 120)
redUpper = (179, 255, 255)

cam.set(3,width)
cam.set(4,height)

# GPIO Setup  

GPIO.setmode(GPIO.BCM)  
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #GPIO of Slave 

def direction_identify(mat):

    l_count=0
    r_count=0

    print 'ok'

    for i in range(height):
        for j in range(width/2):

            if mat[i][j]==255:
                l_count+=1
            if mat[i][j+width/2]==255:
                r_count+=1           

    print
    print "left greencount: " + str(l_count)
    print

    print
    print "Right greencount: " + str(r_count)
    print


# Begin Loop  
try:
    while True:
      
        # frame = imutils.resize(frame, width=600)
        # frame =  cv2.bilateralFilter(frame,9,75,75)
        # cv2.imshow("test", frame)
        # if GPIO.input(23):
        if False:
            # cv2.imshow("test", frame)
        # k = cv2.waitKey(1)    
            ret, frame = cam.read()

            # frame = cv.QueryFrame(capture)
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # print hsv
            # show image


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
        if True:

            print 'line navigation'
           
            ret, frame = cam.read()

            # frame = cv.QueryFrame(capture)
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # print hsv
            # show image


            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)

            # cv2.imwrite('test123.png',blue_mask)
            # print blue_mask
            # mask = blue_mask + green_mask + red_mask
            red_count = 0
            green_count = 0
            blue_count = 0

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
                print red_count
                print
                ser.write('1000')

                if red_count > 100:
                    print 'giya'
                    direction_identify(red_mask)

            elif blue_count > green_count:

                print "blue"

                if blue_count > 100:
                    direction_identify(blue_mask)

            elif green_count>0:

                print "green"
                if green_count > 100:
                    direction_identify(green_mask)

            else:
                print"cant identify"

            for i in range(9):
                ret, frame = cam.read()



    for i in range(10):
        ret, frame = cam.read()

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt    
    GPIO.cleanup() # resets all GPIO ports used by this program



