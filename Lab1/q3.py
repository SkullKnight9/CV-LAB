import cv2 as cv
import numpy as np
import os

img = cv.imread("D:/OpenCV/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

b,g,r = (img[300,300])
print(b)
print(g)
print(r)

# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

cv.waitKey(0)