import cv2

# import imutils
import numpy as np
import RPi.GPIO as GPIO  
import time
import serial

cam = cv2.VideoCapture(0)


while(True):
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200)

        if ser: 
            print 'serial available'
            break
    except:
        print 'serial not available'

height = 240
width= 320
blueLower = (100, 50, 240)
blueUpper = (120, 255, 255)

greenLower = (53, 74, 50)
greenUpper = (90, 147, 255)

redLower = (160, 100, 120)
redUpper = (179, 255, 255)

cam.set(3,width)
cam.set(4,height)

box_color_state = None
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

def robo_adjust(mat):

    l_count=0
    r_count=0
    diff= 0

    print 'ok'

    for i in range(height):
        for j in range(width/2):

            if mat[i][j]==255:
                l_count+=1
            if mat[i][j+width/2]==255:
                r_count+=1           

    # print
    # print "left count: " + str(l_count)
    # print

    # print
    # print "Right count: " + str(r_count)
    # print

    if l_count > r_count:
        ser.write('L')
    
# Begin Loop  
try:
    print 'begin'
    while True:
        state = ser.read()
        print state
        if state == 'k':
            print 'Arduino start communication'
            ser.write('r')
            print 'sent'

        if ser.read() == 'c':
            print 'c recived'
 
            ret, frame = cam.read()
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)

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

            print " "
            print "red_count: " + str(red_count)
            print "greencount: " + str(green_count)
            print "blue count: " + str(blue_count)
            print

            if red_count>blue_count and red_count>green_count:
                print "red"
                box_color_state = "red"
                ser.write('a')
                print 'send the signal a red'

            elif blue_count > green_count:
                print "blue"
                box_color_state = "blue"
                ser.write('a')
                print 'send the signal a blue'

            elif green_count>0:
                print "green"
                box_color_state = "green"
                ser.write('a')
                print 'send the signal a green'

            else:
                print"cant identify"
                ser.write('b')
                print 'no boxes robo go'

            for i in range(9):
                ret, frame = cam.read()

        # if ser.read() == 'k':

        #     print 'box allign'
           
        #     ret, frame = cam.read()
  
        #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #     # print hsv
        #     # show image
        #     if box_color_state == "red"
        #         mask = cv2.inRange(hsv, redLower, redUpper)
        #     elif box_color_state == "blue"
        #         mask = cv2.inRange(hsv, blueLower, blueUpper)
        #     elif box_color_state == "green"
        #         mask = cv2.inRange(hsv, greenLower, greenUpper)        

 
            # robo_adjust(mask)
     
        if False:

            print 'line navigation'
           
            ret, frame = cam.read()
  
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)

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
    ser.close()
    cam.release()




