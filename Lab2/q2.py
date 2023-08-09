import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

img1_path = input("Enter path of first image")
img_ref_path = input("Enter Reference Image path")

img1 = cv.imread(img1_path)
img2 = cv.imread(img_ref_path)

cv.imshow("Image1",img1)
cv.imshow("Image2",img2)

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv


