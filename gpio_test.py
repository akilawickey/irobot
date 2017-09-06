
# import RPi.GPIO as GPIO            # import RPi.GPIO module  
# from time import sleep             # lets us have a delay 
 
# GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
# GPIO.setup(26, GPIO.OUT)  
# GPIO.setup(19, GPIO.OUT) 
# GPIO.setup(13, GPIO.OUT) 
# GPIO.setup(6, GPIO.OUT)          # set GPIO24 as an output   
# GPIO.setup(5, GPIO.OUT) 

# try:  
#     while True:  

#         GPIO.output(26, 1)  
#         GPIO.output(19, 1) 
#         GPIO.output(13, 1) 
#         GPIO.output(6, 1)        # set GPIO24 to 1/GPIO.HIGH/True  
#         GPIO.output(5, 1) 
#         # sleep(0.5)                 # wait half a second  
#         # GPIO.output(37, 0)         # set GPIO24 to 0/GPIO.LOW/False  
#         # sleep(0.5)                 # wait half a second  
  
# except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
#     GPIO.cleanup()                 # resets all GPIO ports used by this program  
# #!/usr/bin/env python

# import os
# from time import sleep

# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)#added pull_up_down
# # # GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP)#added pull_up_down
# # GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)#added pull_up_down

# if GPIO.input(9):
#     print("Pin 9 is HIGH")
# else:
#     print("Pin 9 is LOW")  
import serial
import time

# cam = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyACM0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

while True:

	if ser.read() == 'k':
		print 'got k'
		ser.write('a')
		print 'a sent'
		time.sleep(5)
		print 'sending b'
		ser.write('b')
		time.sleep(5)
		ser.write('a')
		print 'a send'
		time.sleep(5)
		print 'sending b'
		ser.write('b')

ser.close()

