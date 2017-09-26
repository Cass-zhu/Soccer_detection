
#from collections import deque
import argparse
import cv2
#import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# initialize the camera and grab a reference to the raw camera capture
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])

while True:
    #image = frame.array
	(grabbed, frame) = camera.read()
	image = frame
	#frame = imutils.resize(frame, width=600)
	img   = cv2.medianBlur(image, 3)
	imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#imgg  = cv2.blur(imgg, (3,3))
	#imgg = cv2.dilate(imgg, np.ones((5, 5)))
	imgg = cv2.GaussianBlur(imgg,(5,5),0)
	circles = cv2.HoughCircles(imgg, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=45, minRadius=35, maxRadius=90)

	if circles is None:
		continue

	for i in circles[0,:]:
		cv2.circle(imgg,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
		cv2.circle(imgg,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle
		cv2.imshow("Frame", imgg)

	cv2.imshow("Frame", imgg)
	key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
