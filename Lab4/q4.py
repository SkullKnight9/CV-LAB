import numpy as np
import cv2


def kmeans_segmentation(image, k, max_iterations=100):

    pixels = image.reshape(-1, 3).astype(np.float32)

    indices = np.random.choice(len(pixels), k, replace=False)
    centers = pixels[indices]

    for _ in range(max_iterations):
        distances = np.linalg.norm(pixels[:, np.newaxis] - centers, axis=2)

        labels = np.argmin(distances, axis=1)

        new_centers = np.array([pixels[labels == i].mean(axis=0) for i in range(k)])

        if np.all(centers == new_centers):
            break

        centers = new_centers

    segmented_image = centers[labels].reshape(image.shape)

    return segmented_image.astype(np.uint8)



image_path = 'Media/Photos/Park.jpg'
image = cv2.imread(image_path)

num_clusters = 10


segmented_image = kmeans_segmentation(image, num_clusters)

cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
