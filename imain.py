import threading

import cv2

# import imutils
import numpy as np
import RPi.GPIO as GPIO
import time


class ImageDetect(threading.Thread):
    def __init__(self,detectM):
        threading.Thread.__init__(self)
        self.cam = cv2.VideoCapture(0)
        self.height = 240
        self.width = 320
        self.blueLower = (100, 50, 50)
        self.blueUpper = (120, 255, 255)

        self.greenLower = (53, 74, 50)
        self.greenUpper = (90, 147, 255)

        self.redLower = (160, 100, 120)
        self.redUpper = (179, 255, 255)

        self.cam.set(3, self.width)
        self.cam.set(4, self.height)
        self.color = None
        self.lock = threading.Lock()
        self.func = detectM

        # GPIO Setup

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # GPIO of Slave


    def arrow_detect(self,mat):

        l_count = 0
        r_count = 0
        for i in range(self.height):
            for j in range(self.width / 2):

                if mat[i][j] == 255:
                    l_count += 1
                if mat[i][j + self.width / 2] == 255:
                    r_count += 1

        print
        print "left greencount: " + str(l_count)
        print

        print
        print "Right greencount: " + str(r_count)
        print





    def count_mask(self,blue_mask, red_mask, green_mask):
        red_count = 0
        blue_count = 0
        green_count = 0

        for i in range(self.height):
            for j in range(self.width):
                if red_mask[i][j] == 255:
                    red_count += 1
                if green_mask[i][j] == 255:
                    green_count += 1
                if blue_mask[i][j] == 255:
                    blue_count += 1

        return red_count, blue_count, green_count




    def detect_box(self,red_count, blue_count, green_count, red_mask, blue_mask, green_mask):
        color = None
        if red_count > blue_count and red_count > green_count:
            print "red"
            if red_count > 100:
                color = "red"

        elif blue_count > green_count:
            print "blue"
            if blue_count > 100:
                color = "blue"

        elif green_count > 0:
            print "green"
            if green_count > 100:
                color = "green"

        else:
            print"cant identify"

        return color



    def readFrames(self, cam):
        self.lock.acquire()
        ret, frame = self.cam.read()
        self.lock.release()
        return frame


    def runBoxDetect(self):
        print "-----------------------------------------------"
        print "+++++++++++++++ Line Navigation +++++++++++++++"
        print "-----------------------------------------------"

        frame = self.readFrames(self.cam)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # calculate the masks
        blue_mask = cv2.inRange(hsv, self.blueLower, self.blueUpper)
        green_mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
        red_mask = cv2.inRange(hsv, self.redLower, self.redUpper)

        red_count, blue_count, green_count = self.count_mask(blue_mask, red_mask, green_mask)

        print
        print "red_count: " + str(red_count)
        print "greencount: " + str(green_count)
        print "blue count: " + str(blue_count)
        print

        color = self.detect_box(red_count, blue_count, green_count, red_mask, blue_mask, green_mask)
        self.color = color



    def runArrowDetect(self,color):
        print "-----------------------------------------------"
        print "+++++++++++++++ Line Navigation +++++++++++++++"
        print "-----------------------------------------------"
        frame = self.readFrames(self.cam)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = None

        # calculate the masks
        if color == "blue":
            mask = cv2.inRange(hsv, self.blueLower, self.blueUpper)
        if color == "green":
            mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
        if color == "red":
            mask = cv2.inRange(hsv, self.redLower, self.redUpper)

        self.arrow_detect(mask)


    def run(self):
        if self.func == True:
            while True:
                self.runBoxDetect()

        else:
            while True:
                self.readFrames(self.cam)







def main():
    imgp0 = ImageDetect(True)
    imgp1 = ImageDetect(False)
    imgp0.start()
    imgp1.start()


if __name__ == '__main__':
    main()







