import cv2
import numpy as np

class Robo_main:

	def __init__(self):

		self.name = 'Navigating....'

	def camera_feed(self):

		# create video capture
		cap = cv2.VideoCapture(0)
				# Loop to continuously get images
		while(1):
		    # Read the frames frome a camera
		    _,frame = cap.read()
		    # frame = cv2.GaussianBlur(frame,(5,5),0)

		    # show image
		    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		    # thresh = cv2.inRange(hsv,np.array((50, 80, 80)), np.array((120, 255, 255)))
		    # print thresh
		    cv2.imshow('frame', hsv)

		    # if key pressed is 'Esc' then exit the loop
		    if cv2.waitKey(33)== 27:
		    	print 'Bye....'
		        break

				# Clean up and exit the program
			cv2.destroyAllWindows()
			cap.release()



robo = Robo_main()
print robo.name
robo.camera_feed()