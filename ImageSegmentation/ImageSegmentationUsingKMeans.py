# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:28:52 2018

Program: Color Quantization => Process of reducing the number of colors in an image
[k-means clustering for color quantization]

@author: Ankita And Abhilash


"""

import numpy as np
import cv2
import sys




# Reading the images from command line, using cv2.imread() to read an image
#image1 =cv2.imread(sys.argv[1])
#image1 = cv2.imread("Input/image1.jpg")
#image2 = cv2.imread("Input/image2.jpg")
#image3 = cv2.imread("Input/image3.jpg")

image1 = cv2.imread(sys.argv[1])
image2 = cv2.imread(sys.argv[2])
image3 = cv2.imread(sys.argv[3])

# There are 3 features, say, R,G,B. So we need to reshape the image to an array of Mx3 size (M is number of pixels in image

Z1 = image1.reshape((-1,3))
Z2 = image2.reshape((-1,3))
Z3 = image3.reshape((-1,3))

# convert to np.float32
Z1 = np.float32(Z1)
Z2 = np.float32(Z2)
Z3 = np.float32(Z3)

# define criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# define number of clusters(K)
K1 = 5
K2 = 7
K3 = 7


# Apply kmeans()
compactness_image1,clusterLabel_image1,clusterCenter_image1=cv2.kmeans(Z1,K1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
compactness_image2,clusterLabel_image2,clusterCenter_image2=cv2.kmeans(Z2,K2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
compactness_image3,clusterLabel_image3,clusterCenter_image3=cv2.kmeans(Z3,K3,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
clusterCenter_image1 = np.uint8(clusterCenter_image1)
res_image1 = clusterCenter_image1[clusterLabel_image1.flatten()]
clustered_image1 = res_image1.reshape((image1.shape))

clusterCenter_image2 = np.uint8(clusterCenter_image2)
res_image2 = clusterCenter_image2[clusterLabel_image2.flatten()]
clustered_image2 = res_image2.reshape((image2.shape))

clusterCenter_image3 = np.uint8(clusterCenter_image3)
res_image3 = clusterCenter_image3[clusterLabel_image3.flatten()]
clustered_image3 = res_image3.reshape((image3.shape))


# Write images
cv2.imwrite('Clustered_image1.jpg',clustered_image1)
cv2.imwrite('Clustered_image2.jpg',clustered_image2)
cv2.imwrite('Clustered_image3.jpg',clustered_image3)

# Display images
cv2.imshow('Clustered_image1', clustered_image1)
cv2.imshow('Clustered_image2', clustered_image2)
cv2.imshow('Clustered_image3', clustered_image3)


cv2.waitKey(0)

# destroys all the windows that are created.
cv2.destroyAllWindows()



