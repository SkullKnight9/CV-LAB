import cv2 as cv
import numpy as np

img = cv.imread('C:/210962140/venv/Media/Photos/rose.jpg')
cv.imshow("Original Image",img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsv)

lower_red = np.array([0,50,70])
upper_red = np.array([9,255,255])

mask = cv.inRange(hsv, lower_red, upper_red)

res = cv.bitwise_and(img,img,mask=mask)

cv.imshow("Result",res)
cv.imshow("Mask",mask)

cv.waitKey()