import cv2
import imutils
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


ret, frame = cam.read()
# cv2.imshow("test", frame)
k = cv2.waitKey(1)

# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# show image
blueLower = (98, 109, 20)
blueUpper = (112, 255, 255)
frame = imutils.resize(frame, width=600)
frame =  cv2.bilateralFilter(frame,9,75,75)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# blobs left in the mask
# cv2.imshow('hsv', hsv)

mask = cv2.inRange(fame, blueLower, blueUpper)
mask = cv2.inRange(frame, blueLower, blueUpper)

mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
image, contours, hier = cv2.findContours(mask, cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
	# get the bounding rect
	x, y, w, h = cv2.boundingRect(c)
	# draw a green rectangle to visualize the bounding rect
	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# get the min area rect
	rect = cv2.minAreaRect(c)
	box = cv2.boxPoints(rect)
	# convert all coordinates floating point values to int
	box = np.int0(box)
	# draw a red 'nghien' rectangle
	cv2.drawContours(frame, [box], 0, (0, 0, 255))
	print 'Blue box detected'

print(len(contours))


# # SPACE pressed
# img_name = "opencv_frame_{}.png".format(img_counter)
# # cv2.imwrite(img_name, frame)
# print("{} written!".format(img_name))
# img_counter += 1

cam.release()

cv2.destroyAllWindows()