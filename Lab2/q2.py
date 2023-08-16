import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    # We need to mask the negative differences
    # since we are looking for values above
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c # returns min index of the nearest if target is greater than any value
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()


def hist_match(original, specified):
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()

    # get the set of unique pixel values and their corresponding indices and counts
    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)

    # Calculate s_k for original image
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]

    # Calculate s_k for specified image
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # Round the values
    sour = np.around(s_quantiles * 255)
    temp = np.around(t_quantiles * 255)

    # Map the rounded values
    b = []
    for data in sour[:]:
        b.append(find_nearest_above(temp, data))
    b = np.array(b, dtype='uint8')

    return b[bin_idx].reshape(oldshape)


# Load the images in greyscale
original = cv.imread('C:/210962140/venv/Media/Photos/Park.jpg',0)
specified = cv.imread('C:/210962140/venv/Media/Photos/cat.jpg',0)

# perform Histogram Matching
a = hist_match(original, specified)

# Display the image
cv.imshow('a',np.array(a,dtype='uint8'))
cv.imshow('a1',original)
cv.imshow('a2',specified)

original1 = cv.calcHist([original],[0],None,[256],[0,256])
specified1 = cv.calcHist([specified],[0],None,[256],[0,256])
a1 = cv.calcHist([a],[0],None,[256],[0,256])

plt.figure()

plt.plot(original1)
plt.xlim([0,256])
plt.title("Histogram for Original Image")


plt.figure()
plt.plot(specified1)
plt.xlim([0,256])
plt.title("Histogram for Reference Image Image")
plt.show()

plt.figure()
plt.plot(a1)
plt.xlim([0,256])
plt.title("Histogram for Equalized Image")
plt.show()

cv.waitKey(0)




