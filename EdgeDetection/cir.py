import numpy as np
import cv2 as cv
img = cv.imread('cir2.jpg',0)
img = cv.medianBlur(img,15)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
edge = cv.Canny(cimg,70,120)
circles = cv.HoughCircles(edge,cv.HOUGH_GRADIENT,100,150,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint64(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',img)
cv.waitKey(0)
cv.destroyAllWindows()