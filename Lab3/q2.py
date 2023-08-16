import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")
cv.imshow('Image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)



sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)


cv.imshow("Combined Sobel", combined_sobel)
cv.imshow("Sobel X",sobelx)
cv.imshow("Sobel Y", sobely)


cv.waitKey()