import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

img = cv.imread('C:/210962140/venv/Media/Photos/Park.jpg',0)
#cv.imshow("Park", img)
gray = img
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)

#Grayscale histogram
#gray_hist = cv.calcHist(gray,[0],None, [256], [0,256])

plt.figure()
hist,bins = np.histogram(gray.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(gray.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.title("Histogram for a Grayscale Image")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.show()

dst = cv.equalizeHist(gray)
cv.imshow('Equalized Image',dst)

plt.figure()
hist,bins = np.histogram(dst.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(dst.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.title("Histogram for an Equalized Image")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

plt.show()

cv.waitKey(0)