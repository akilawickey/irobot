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

        if ser.isOpen(): 
            print 'serial available'
            break
    except:
        print 'serial not available'

ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
ser = serial.Serial('/dev/ttyACM0', 115200)

height = 240
width= 320
# blueLower = (100, 50, 240)
# blueUpper = (120, 255, 255)

# greenLower = (53, 74, 50)
# greenUpper = (90, 147, 255)

# redLower = (160, 100, 120)
# redUpper = (179, 255, 255)
blueLower = (100, 50, 50)
blueUpper = (120, 255, 255)

greenLower = (53, 150, 0)
greenUpper = (90, 255, 255)

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

    for i in range(height*3/4):
        for j in range(width/2):

            if mat[i][j]==255:
                l_count+=1
            if mat[i][j+width/2]==255:
                r_count+=1           

    print
    print "left pixel count: naviagation " + str(l_count)
    print

    print
    print "Right pixel count: naviagation " + str(r_count)
    print

    diff = abs(r_count - l_count)
    diff = (diff/(r_count+l_count))*100


    if l_count > r_count and diff > 10:
        print 'sending L'
        ser.write('L')
        print 'sent L'

    elif r_count > l_count and diff >10:
        print 'sending R'
        ser.write('R')
        print 'sent R'

    elif diff <= 10:
        print 'sending M'
        ser.write('M')
        print 'sent M'


def robo_adjust(mat):

    l_count=0
    r_count=0
    diff= 0

    print 'ok'

    for i in range(height - 30,height):
        for j in range(width/2):

            if mat[i][j]==255:
                l_count+=1
            if mat[i][j+width/2]==255:
                r_count+=1           

    diff = abs(r_count - l_count)
    diff = (diff/(r_count+l_count))*100


    if l_count > r_count and diff > 10:
        print 'sending L'
        ser.write('L')
        print 'sent L'

    elif r_count > l_count and diff >10:
        print 'sending R'
        ser.write('R')
        print 'sent R'

    elif diff <= 10:
        print 'sending M'
        ser.write('M')
        print 'sent M'
    
# Begin Loop  
try:
    print 'begin'
    while True:
        state = ser.read()
        # state = 'e'
        print state
        if state == 'k':
            print 'Arduino start communication'
            ser.write('r')
            print 'sent'

        if state == 'c':
            print 'c recived'
 
            ret, frame = cam.read()
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
            blue_mask = cv2.inRange(hsv, blueLower, blueUpper)
            green_mask = cv2.inRange(hsv, greenLower, greenUpper)
            red_mask = cv2.inRange(hsv, redLower, redUpper)

            red_count=0
            blue_count=0
            green_count=0

            for i in range(height-30, height):
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

            threashold = 100

            if red_count>blue_count and red_count>green_count and red_count > threashold:
                print "red"
                box_color_state = "red"
                ser.write('a')
                print 'send the signal a red'

            elif blue_count > green_count and blue_count > threashold:
                print "blue"
                box_color_state = "blue"
            
                ser.write('a')
                print 'send the signal a blue'

            elif green_count>0 and green_count > threashold:
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

        if state == 'z':

            print 'box allign'
           
            ret, frame = cam.read()
  
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # print hsv
            # show image

            if box_color_state == "red":
                mask = cv2.inRange(hsv, redLower, redUpper)
                robo_adjust(mask)
            elif box_color_state == "blue":
                mask = cv2.inRange(hsv, blueLower, blueUpper)
                robo_adjust(mask)
            elif box_color_state == "green":
                mask = cv2.inRange(hsv, greenLower, greenUpper)  
                robo_adjust(mask)      

 
           
     
        if state == 'e':

            print 'line navigation'
           
            ret, frame = cam.read()
  
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # print hsv
            # show image
            # box_color_state = "green"

            if box_color_state == "red":
                mask = cv2.inRange(hsv, redLower, redUpper)
                direction_identify(mask)

            elif box_color_state == "blue":
                mask = cv2.inRange(hsv, blueLower, blueUpper)
                direction_identify(mask)

            elif box_color_state == "green":
                mask = cv2.inRange(hsv, greenLower, greenUpper)  
                cv2.imshow('image',mask)
                direction_identify(mask)

            for i in range(20):
                ret, frame = cam.read()



    for i in range(20):
        ret, frame = cam.read()

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt    
    GPIO.cleanup() # resets all GPIO ports used by this program
    ser.close()
    cam.release()




