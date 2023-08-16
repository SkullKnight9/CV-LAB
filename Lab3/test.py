import cv2 as cv
import numpy as np

image = cv.imread("C:/210962140/venv/Media/Photos/Cats.jpg")

# Applying Identity Kernel

kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])

identity = cv.filter2D(src=image,ddepth=-1,kernel=kernel1)

cv.imshow("Original", image)
cv.imshow('Identity', identity)


cv.imwrite('Identity.jpg', identity)

# Apply blurring kernel

kernel2 = np.ones((5,5),np.float32)/25
img = cv.filter2D(src=image,ddepth=-1,kernel=kernel2)

cv.imshow('Original',image)
cv.imshow('Kernel Blur',img)

cv.waitKey()
