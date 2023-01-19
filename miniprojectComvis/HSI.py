from pickletools import unicodestring8
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread("ly.jpg")

MAX_G = 256
h,w,s = img.shape
h2 = int((h/2))
w2 = int((w/2))

red = 255
green = 255
blue = 255

def hsi(img):
    hsi = np.zeros([h,w,s])
    for i in range(0,h2):
        for j in range(0,w2):
            if(img[i,j,2]*1+img[i,j,1]*1+img[i,j,0]*1 == 0):
                hsi[i,j,0] = 240
                hsi[i,j,1] = 0
                hsi[i,j,2] = 0
            else:
                r = img[i,j,2]*1/(img[i,j,2]*1+img[i,j,1]*1+img[i,j,0]*1)
                g = img[i,j,1]*1/(img[i,j,2]*1+img[i,j,1]*1+img[i,j,0]*1)
                b = img[i,j,0]*1/(img[i,j,2]*1+img[i,j,1]*1+img[i,j,0]*1)
                if (b <= g):
                    H = (np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                else:
                    H = (360 - np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                S = (1-3*min(r,g,b))*100
                I = (img[i,j,2]*1+img[i,j,1]*1+img[i,j,0]*1)/3
                hsi[i,j,0] = H
                hsi[i,j,1] = S
                hsi[i,j,2] = I

            if(img[h2+i,j,2]*1+img[h2+i,j,1]*1+img[h2+i,j,0]*1 == 0):
                hsi[h2+i,j,0] = 240
                hsi[h2+i,j,1] = 0
                hsi[h2+i,j,2] = 0
            else:
                r = img[h2+i,j,2]*1/(img[h2+i,j,2]*1+img[h2+i,j,1]*1+img[h2+i,j,0]*1)
                g = img[h2+i,j,1]*1/(img[h2+i,j,2]*1+img[h2+i,j,1]*1+img[h2+i,j,0]*1)
                b = img[h2+i,j,0]*1/(img[h2+i,j,2]*1+img[h2+i,j,1]*1+img[h2+i,j,0]*1)
                if (b <= g):
                    H = (np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                else:
                    H = (360 - np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                S = (1-3*min(r,g,b))*100
                I = (img[h2+i,j,2]*1+img[h2+i,j,1]*1+img[h2+i,j,0]*1)/3
                hsi[h2+i,j,0] = H
                hsi[h2+i,j,1] = S
                hsi[h2+i,j,2] = I

            if(img[i,w2+j,2]*1+img[i,w2+j,1]*1+img[i,w2+j,0]*1 == 0):
                hsi[i,w2+j,0] = 240
                hsi[i,w2+j,1] = 0
                hsi[i,w2+j,2] = 0
            else:
                r = img[i,w2+j,2]*1/(img[i,w2+j,2]*1+img[i,w2+j,1]*1+img[i,w2+j,0]*1)
                g = img[i,w2+j,1]*1/(img[i,w2+j,2]*1+img[i,w2+j,1]*1+img[i,w2+j,0]*1)
                b = img[i,w2+j,0]*1/(img[i,w2+j,2]*1+img[i,w2+j,1]*1+img[i,w2+j,0]*1)
                if (b <= g):
                    H = (math.acos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                else:
                    H = (360 - np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                S = (1-3*min(r,g,b))*100
                I = (img[i,w2+j,2]*1+img[i,w2+j,1]*1+img[i,w2+j,0]*1)/3
                hsi[i,w2+j,0] = H
                hsi[i,w2+j,1] = S
                hsi[i,w2+j,2] = I

            if(img[h2+i,w2+j,2]*1+img[h2+i,w2+j,1]*1+img[h2+i,w2+j,0]*1 == 0):
                hsi[h2+i,w2+j,0] = 240
                hsi[h2+i,w2+j,1] = 0
                hsi[h2+i,w2+j,2] = 0
            else:
                r = img[h2+i,w2+j,2]*1/(img[h2+i,w2+j,2]*1+img[h2+i,w2+j,1]*1+img[h2+i,w2+j,0]*1)
                g = img[h2+i,w2+j,1]*1/(img[h2+i,w2+j,2]*1+img[h2+i,w2+j,1]*1+img[h2+i,w2+j,0]*1)
                b = img[h2+i,w2+j,0]*1/(img[h2+i,w2+j,2]*1+img[h2+i,w2+j,1]*1+img[h2+i,w2+j,0]*1)
                if (b <= g):
                    H = (np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                else:
                    H = (360 - np.arccos(round((0.5*(r-g+r-b))/math.sqrt((r-g)**2+((r-b)*(g-b))),3)))*180/math.pi
                S = (1-3*min(r,g,b))*100
                I = (img[h2+i,w2+j,2]*1+img[h2+i,w2+j,1]*1+img[h2+i,w2+j,0]*1)/3
                hsi[h2+i,w2+j,0] = H
                hsi[h2+i,w2+j,1] = S
                hsi[h2+i,w2+j,2] = I
            
    return hsi

def colorhue(hsi,hue1,hue2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                newimg[i,j,0] = img[i,j,0]
                newimg[i,j,1] = img[i,j,1]
                newimg[i,j,2] = img[i,j,2]
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                newimg[h2+i,j,0] = img[h2+i,j,0]
                newimg[h2+i,j,1] = img[h2+i,j,1]
                newimg[h2+i,j,2] = img[h2+i,j,2]

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                newimg[i,w2+j,0] = img[i,w2+j,0]
                newimg[i,w2+j,1] = img[i,w2+j,1]
                newimg[i,w2+j,2] = img[i,w2+j,2]

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                newimg[h2+i,w2+j,0] = img[h2+i,w2+j,0]
                newimg[h2+i,w2+j,1] = img[h2+i,w2+j,1]
                newimg[h2+i,w2+j,2] = img[h2+i,w2+j,2]
    return newimg

def detechue(hsi,hue1,hue2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    newimg = img
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                newimg[i,j,0] = blue
                newimg[i,j,1] = green
                newimg[i,j,2] = red
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                newimg[h2+i,j,0] = blue
                newimg[h2+i,j,1] = green
                newimg[h2+i,j,2] = red

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                newimg[i,w2+j,0] = blue
                newimg[i,w2+j,1] = green
                newimg[i,w2+j,2] = red

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                newimg[h2+i,w2+j,0] = blue
                newimg[h2+i,w2+j,1] = green
                newimg[h2+i,w2+j,2] = red
    return newimg

def saturation(hsi,hue1,hue2,sat1,sat2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                if(hsi[i,j,1] >= sat1 and hsi[i,j,1] <= sat2):
                    newimg[i,j,0] = img[i,j,0]
                    newimg[i,j,1] = img[i,j,0]
                    newimg[i,j,2] = img[i,j,0]
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                if(hsi[h2+i,j,1] >= sat1 and hsi[h2+i,j,1] <= sat2):
                    newimg[h2+i,j,0] = img[h2+i,j,0]
                    newimg[h2+i,j,1] = img[h2+i,j,1]
                    newimg[h2+i,j,2] = img[h2+i,j,2]

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                if(hsi[i,w2+j,1] >= sat1 and hsi[i,w2+j,1] <= sat2):
                    newimg[i,w2+j,0] = img[i,w2+j,0]
                    newimg[i,w2+j,1] = img[i,w2+j,1]
                    newimg[i,w2+j,2] = img[i,w2+j,2]

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                if(hsi[h2+i,w2+j,1] >= sat1 and hsi[h2+i,w2+j,1] <= sat2):
                    newimg[h2+i,w2+j,0] = img[h2+i,w2+j,0]
                    newimg[h2+i,w2+j,1] = img[h2+i,w2+j,1]
                    newimg[h2+i,w2+j,2] = img[h2+i,w2+j,2]
    return newimg

def deSaturation(hsi,hue1,hue2,sat1,sat2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    newimg = img
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                if(hsi[i,j,1] >= sat1 and hsi[i,j,1] <= sat2):
                    newimg[i,j,0] = blue
                    newimg[i,j,1] = green
                    newimg[i,j,2] = red
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                if(hsi[h2+i,j,1] >= sat1 and hsi[h2+i,j,1] <= sat2):
                    newimg[h2+i,j,0] = blue
                    newimg[h2+i,j,1] = green
                    newimg[h2+i,j,2] = red

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                if(hsi[i,w2+j,1] >= sat1 and hsi[i,w2+j,1] <= sat2):
                    newimg[i,w2+j,0] = blue
                    newimg[i,w2+j,1] = green
                    newimg[i,w2+j,2] = red

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                if(hsi[h2+i,w2+j,1] >= sat1 and hsi[h2+i,w2+j,1] <= sat2):
                    newimg[h2+i,w2+j,0] = blue
                    newimg[h2+i,w2+j,1] = green
                    newimg[h2+i,w2+j,2] = red
    return newimg

def intensity(hsi,hue1,hue2,sat1,sat2,inten1,inten2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                if(hsi[i,j,1] >= sat1 and hsi[i,j,1] <= sat2):
                    if(hsi[i,j,2] >= inten1 and hsi[i,j,2] <= inten2):
                        newimg[i,j,0] = img[i,j,0]
                        newimg[i,j,1] = img[i,j,0]
                        newimg[i,j,2] = img[i,j,0]
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                if(hsi[h2+i,j,1] >= sat1 and hsi[h2+i,j,1] <= sat2):
                    if(hsi[h2+i,j,2] >= inten1 and hsi[h2+i,j,2] <= inten2):
                        newimg[h2+i,j,0] = img[h2+i,j,0]
                        newimg[h2+i,j,1] = img[h2+i,j,1]
                        newimg[h2+i,j,2] = img[h2+i,j,2]

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                if(hsi[i,w2+j,1] >= sat1 and hsi[i,w2+j,1] <= sat2):
                    if(hsi[i,w2+j,2] >= inten1 and hsi[i,w2+j,2] <= inten2):
                        newimg[i,w2+j,0] = img[i,w2+j,0]
                        newimg[i,w2+j,1] = img[i,w2+j,1]
                        newimg[i,w2+j,2] = img[i,w2+j,2]

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                if(hsi[h2+i,w2+j,1] >= sat1 and hsi[h2+i,w2+j,1] <= sat2):
                    if(hsi[h2+i,w2+j,2] >= inten1 and hsi[h2+i,w2+j,2] <= inten2):
                        newimg[h2+i,w2+j,0] = img[h2+i,w2+j,0]
                        newimg[h2+i,w2+j,1] = img[h2+i,w2+j,1]
                        newimg[h2+i,w2+j,2] = img[h2+i,w2+j,2]
    return newimg

def deIntensity(hsi,hue1,hue2,sat1,sat2,inten1,inten2):
    newimg = np.zeros([h,w,s],dtype=np.uint8)
    newimg = img
    for i in range(0,h2):
        for j in range(0,w2):
            if(hsi[i,j,0]>=hue1 and hsi[i,j,0]<=hue2):
                if(hsi[i,j,1] >= sat1 and hsi[i,j,1] <= sat2):
                    if(hsi[i,j,2] >= inten1 and hsi[i,j,2] <= inten2):
                        newimg[i,j,0] = blue
                        newimg[i,j,1] = green
                        newimg[i,j,2] = red
            
            if(hsi[h2+i,j,0]>=hue1 and hsi[h2+i,j,0]<=hue2):
                if(hsi[h2+i,j,1] >= sat1 and hsi[h2+i,j,1] <= sat2):
                    if(hsi[h2+i,j,2] >= inten1 and hsi[h2+i,j,2] <= inten2):
                        newimg[h2+i,j,0] = blue
                        newimg[h2+i,j,1] = green
                        newimg[h2+i,j,2] = red

            if(hsi[i,w2+j,0]>=hue1 and hsi[i,w2+j,0]<=hue2):
                if(hsi[i,w2+j,1] >= sat1 and hsi[i,w2+j,1] <= sat2):
                    if(hsi[i,w2+j,2] >= inten1 and hsi[i,w2+j,2] <= inten2):
                        newimg[i,w2+j,0] = blue
                        newimg[i,w2+j,1] = green
                        newimg[i,w2+j,2] = red

            if(hsi[h2+i,w2+j,0]>=hue1 and hsi[h2+i,w2+j,0]<=hue2):
                if(hsi[h2+i,w2+j,1] >= sat1 and hsi[h2+i,w2+j,1] <= sat2):
                    if(hsi[h2+i,w2+j,2] >= inten1 and hsi[h2+i,w2+j,2] <= inten2):
                        newimg[h2+i,w2+j,0] = blue
                        newimg[h2+i,w2+j,1] = green
                        newimg[h2+i,w2+j,2] = red
    return newimg

HSI = hsi(img)
imgHue1 = intensity(HSI,30,150,0,100,0,255)
cv2.imshow("test1",imgHue1)
imgHue2 = deIntensity(HSI,30,150,0,100,0,255)
cv2.imshow("test2",imgHue2)
cv2.waitKey(0)