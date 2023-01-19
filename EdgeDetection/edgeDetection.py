"""
ผู้จัดทำ 
    นายภูผา ไชยดี 63172310444-1
    นายวัฒนา นามมา 6317310369-7
    นายณัฐพงศ์ เสาวพันธ์ 63172310241-3
    นายกวี นวลสุธา 63172310242-3
    นายอนันตภพ โค่นถอน 63172310156-1
"""


from itertools import count
import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from scipy import ndimage  

imgpa = 'stl2.jpg'

Rres = 1
Thetares = 1*np.pi/180
Threshold = 100
minLineLength = 5
maxLineGap = 10

def robert(imgpa):
    roberts_cross_v = np.array( [[1,0],[0,-1]] )
    roberts_cross_h = np.array( [[0,1],[-1,0]] )
    
    robert = cv2.imread(imgpa,0).astype('float64')
    robert/=255.0
    vertical = ndimage.convolve( robert, roberts_cross_v )
    horizontal = ndimage.convolve( robert, roberts_cross_h )
    edged_img_robert = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img_robert*=255

    return edged_img_robert

def sobel(imgpa):
    sobel_cross_v = np.array( [[1,0,-1],
                             [2,0,-2 ],
                             [1,0,-1]] )

    sobel_cross_h = np.array( [[1, 2, 1 ],
                             [ 0, 0, 0 ],
                             [-1,-2,-1]] )
    
    sobel = cv2.imread(imgpa,0).astype('float64')
    sobel/=255.0
    vertical = ndimage.convolve( sobel, sobel_cross_v )
    horizontal = ndimage.convolve( sobel, sobel_cross_h )
    edged_img_sobel = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img_sobel*=255

    return edged_img_sobel

def prewitt(imgpa):
    prewitt_cross_v = np.array( [[1,0,-1],
                             [1,0,-1 ],
                             [1,0,-1]] )

    prewitt_cross_h = np.array( [[1, 1, 1 ],
                             [ 0, 0, 0 ],
                             [-1,-1,-1]] )
    
    prewitt = cv2.imread(imgpa,0).astype('float64')
    prewitt/=255.0
    vertical = ndimage.convolve( prewitt, prewitt_cross_v )
    horizontal = ndimage.convolve( prewitt, prewitt_cross_h )
    edged_img_prewitt = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img_prewitt*=255

    return edged_img_prewitt

def canny(imgpa):
    img = cv.imread(imgpa,0)
    edgesCanny = cv.Canny(img,150,350)

    return edgesCanny

def showImg(imgpa):
    cannyim = canny(imgpa)
    robertim = robert(imgpa)
    prewittim = prewitt(imgpa)
    sobelim = sobel(imgpa)

    img = cv.imread(imgpa,0)

    plt.subplot(231),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(232),plt.imshow(cannyim,cmap = 'gray')
    plt.title('Canny'), plt.xticks([]), plt.yticks([])

    plt.subplot(233),plt.imshow(robertim,cmap = 'gray')
    plt.title('Robert'), plt.xticks([]), plt.yticks([])

    plt.subplot(234),plt.imshow(prewittim,cmap = 'gray')
    plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

    plt.subplot(235),plt.imshow(sobelim,cmap = 'gray')
    plt.title('Sobel'), plt.xticks([]), plt.yticks([])
    
    plt.show()

    cv2.imwrite('circanny.jpg',cannyim)
    cv2.imwrite('cirrobert.jpg',robertim)
    cv2.imwrite('cirprewitt.jpg',prewittim)
    cv2.imwrite('cirsobel.jpg',sobelim)

showImg(imgpa)


