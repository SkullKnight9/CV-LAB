import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:/210962140/venv/Media/Photos/chessboard.jpg', cv.IMREAD_GRAYSCALE)

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()

# find and draw the keypoints


kp = fast.detect(img, None)
img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))

# Print all default params
print("Threshold: {}".format(fast.getThreshold()))
print("non maxSuppression:{}".format(fast.getNonmaxSuppression()))
print("neighborhood: {}".format(fast.getType()))
print("Total Keypoints with non maxSuppression: {}".format(len(kp)))

cv.imwrite('fast_true.png', img2)

fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print("Total Keypoints without non maxSuppression: {}".format(len(kp)))
img3 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
cv.imwrite('fast_false.png', img3)

cv.waitKey()
