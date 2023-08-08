import cv2 as cv
import numpy as np
import os

img = cv.imread("D:/OpenCV/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

img_big = cv.resize(img,(1050,1610))
cv.imshow("Bigger",img_big)

img_interpolated = cv.resize(img, (780,540), interpolation=cv.INTER_LINEAR)
cv.imshow("Interpolated",img_interpolated)


cv.waitKey(0)