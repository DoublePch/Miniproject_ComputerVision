import cv2
import numpy as np
import math

def RGB2HSI(img,H,S,I):

    rows=int (img.shape [0])
    cols=int (img.shape [1])


    b,g,r = cv2.split(img)
    

    print("r = ",r)
    print("g = ",g)
    print("b = ",b)
    red = r/(3*255)
    green = g/(3*255)
    blue = b/(3*255)
    B = b/(r+g+b)
    G = g/(r+g+b)
    R = r/(r+g+b)

    
    def saturation(r,g,b):
        minimum = np.minimum(np.minimum(r, g), b)
        s = 1 - (3 / (r + g + b) * minimum)
        print("S = ",s)
        return s*100

    def hue(red,green,blue):
        h = np.copy(red)
        for i in range (rows):
            for j in range (cols):
                h[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / math.sqrt((red[i][j] - green[i][j])**2 + ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                h[i][j] = math.acos(h[i][j])
                if blue[i][j] <= green[i][j]:
                    h[i][j] = h[i][j]
                else:
                    h[i][j] = (2*math.pi) - h[i][j]
        print("H = ",h*180/math.pi)
        return h*180/math.pi


    hu = hue(R,G,B)
    sat = saturation(R,G,B)
    inten = (red+green+blue)*255

    print("Hue = ", hu)
    print("Sat = ", sat)
    print("Intensity = ",inten)

    hsi = cv2.merge((hu, sat,inten))
    
    if 181 <= H <= 240:
        arrayH = hu
    else:
        arrayH = 0
    if 0 <= S <= 100:
        arrayS = sat
    else:
        arrayS = 0
    if 0 <= I <= 255:
        arrayI = inten
    else:
        arrayI = 0


    print(arrayH)
    print(arrayS)
    print(arrayI)

    hsi = cv2.merge((arrayH,arrayS,arrayI))
    

    return hsi