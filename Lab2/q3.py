import cv2 as cv
import numpy as np
import os

img = cv.imread("C:/210962140/venv/Media/Photos/Park.jpg")
cv.imshow("Cats",img)

#img_big = cv.resize(img,(1050,1610))
#cv.imshow("Bigger",img_big)

img_interpolated = cv.resize(img, (780,540), interpolation=cv.INTER_LINEAR)
cv.imshow("Interpolated",img_interpolated)

#cropping Image

cropped_image = img[80:280, 150:330]
cv.imshow("Cropped Image",cropped_image)

cv.waitKey(0)