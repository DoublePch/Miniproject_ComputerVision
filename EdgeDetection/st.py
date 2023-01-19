from itertools import count
import cv2
from cv2 import edgePreservingFilter
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from scipy import ndimage 

count = 0
img = cv.imread('hh.jpg',0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edgesCanny = cv2.Canny(gray,300,400,apertureSize=3)

lines_list =[]
lines = cv2.HoughLinesP(edgesCanny,1, np.pi/180, threshold=100, minLineLength=5,maxLineGap=10)
for points in lines:
    x1,y1,x2,y2=points[0] 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
    lines_list.append([(x1,y1),(x2,y2)])
    count+=1
cv2.imshow(cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2))