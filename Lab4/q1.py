import cv2 as cv

img = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")
cv.imshow("Cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Simple Thresholding

threshold1, thresh = cv.threshold(gray,100,255, cv.THRESH_BINARY)
cv.imshow(" Simple Thresh-holded Image",thresh)

threshold2, thresh_inv = cv.threshold(gray,100,255, cv.THRESH_BINARY_INV)
cv.imshow(" Simple  Inverted Thresh-holded Image",thresh_inv)

threshold3, thresh_trunc = cv.threshold(gray,100,255,cv.THRESH_TRUNC)
cv.imshow('Trunc Thresh-holding',thresh_trunc)

threshold4, thresh_tozero = cv.threshold(gray,100,255,cv.THRESH_TOZERO)
cv.imshow('Tozero Thresh-holding',thresh_tozero)

threshold5, thresh_tozero_inv = cv.threshold(gray,100,255,cv.THRESH_TOZERO_INV)
cv.imshow('Tozero Thresh-holding inverted',thresh_tozero_inv)

# Adaptive Thresholding

adpative_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding",adpative_thresh)



cv.waitKey(0)
