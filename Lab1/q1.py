import cv2 as cv
import numpy as np
import os

img = cv.imread("D:/OpenCV/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

image_path = r"D:/OpenCV/Media/Photos/Cats.jpg"

os.chdir("D:/CV Lab/Lab1")

filename = 'Cats.jpg'

cv.imwrite(filename,img)


cv.waitKey(0)

