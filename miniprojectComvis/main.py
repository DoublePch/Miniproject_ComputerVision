"""
ผู้จัดทำ 
    นายภูผา ไชยดี 63172310444-1
    นายวัฒนา นามมา 6317310369-7
    นายณัฐพงศ์ เสาวพันธ์ 63172310241-3
    นายกวี นวลสุธา 63172310242-3
    นายอนันตภพ โค่นถอน 63172310156-1
"""
import cv2
import rgb2hsi

img = cv2.imread('1.jpg',1)

H = int(input("H = "))
S = int(input("S = "))
I = int(input("I = "))

hsi = rgb2hsi.RGB2HSI(img,H,S,I)

cv2.imshow('Base Image', img)
# Display HSV Image
cv2.imshow('HSI Image', hsi)

cv2.waitKey(0)
cv2.destroyAllWindows()



