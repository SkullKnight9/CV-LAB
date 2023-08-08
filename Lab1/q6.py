import cv2 as cv
import numpy as np
import os

img = cv.imread("D:/OpenCV/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

img_rotate = cv.rotate(img, cv.ROTATE_180)
cv.imshow("Rotated Image",img_rotate)


cv.waitKey(0)
