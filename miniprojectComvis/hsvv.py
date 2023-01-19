import cv2 
import numpy as np

img = cv2.imread("ly.jpg",1)
    # Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
lower_blue = np.array([10,20,20])
upper_blue = np.array([140,255,90])
    # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
  