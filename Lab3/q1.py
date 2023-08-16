import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")
cv.imshow('Image',img)

guassian = cv.GaussianBlur(img, (3,3), 0)
unsharp_image = cv.addWeighted(img,2,guassian,-1,0)   # Eqn applied on image --> img = a . img1 + b . img 2 + y

cv.imshow("Gaussian Blur",guassian)
cv.imshow("Unsharpened Image",unsharp_image)
cv.waitKey(0)
