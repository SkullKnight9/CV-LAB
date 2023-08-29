import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv.imread("Media/Photos/Sudoku.png")

def rescaleFrame(frame, scale=0.50):
    width = int(frame.shape[1] * scale)  # frame.shape[1] width of img
    height = int(frame.shape[0] * scale)  # frame.shape[0] height of img

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow("Image", resized_image)

gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

edge_detection = cv.Canny(gray,50,200,None,3)
cdst = cv.cvtColor(edge_detection, cv.COLOR_GRAY2BGR)
#cv.imshow("Edges on the BGR Image", cdst)
cv.imshow("Edges",edge_detection)

# plt.figure()
# plt.imshow(np.asarray(cdst))
# plt.show()
#
# plt.figure()
# plt.imshow(np.asarray(edge_detection))
# plt.show()

lines = cv.HoughLines(edge_detection, 1, np.pi/180, 200)
for i in range(0, len(lines)):
  rho = lines[i][0][0]
  theta = lines[i][0][1]
  a = math.cos(theta)
  b = math.sin(theta)
  x0 = a * rho
  y0 = b * rho
  pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
  pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

  cv.line(cdst, pt1, pt2, (0, 0, 255), 1, cv.LINE_AA)
  cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)

cv.waitKey()
