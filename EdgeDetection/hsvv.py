"""
ผู้จัดทำ
    นายภูผา ไชยดี 63172310444-1
    นายวัฒนา นามมา 6317310369-7
    นายณัฐพงศ์ เสาวพันธ์ 63172310241-3
    นายกวี นวลสุธา 63172310242-3
    นายอนันตภพ โค่นถอน 63172310156-1
"""
import cv2
import numpy as np

img = cv2.imread("ly.jpg",1)
    # Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
lower = np.array([10,20,20])
upper = np.array([140,255,90])
    # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower, upper)
    # Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
