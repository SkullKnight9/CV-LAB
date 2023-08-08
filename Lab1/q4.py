import cv2 as cv
import numpy as np
import os

img = cv.imread("D:/OpenCV/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

blank = np.zeros((500,500), dtype='uint8')

cv.rectangle(img,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow("Rectangle1",img)

cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=2)
cv.imshow("Rectangle2",blank)

cv.waitKey(0)