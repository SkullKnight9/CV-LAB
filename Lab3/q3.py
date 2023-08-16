import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")
cv.imshow('Image',img)

gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("Gaussian",gauss)

blur = cv.blur(img,(5,5))
cv.imshow('Blurred Image',blur)


cv.waitKey()