import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")
cv.imshow('Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)