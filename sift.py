import cv2
import numpy as np
from matplotlib import pyplot as plt

image1 = cv2.imread('queries\q1.jpg')
image2 = cv2.imread('queries\q2.jpg')
cv2.imshow('img1', image1)
cv2.imshow('img2', image2)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

image1 = cv2.drawKeypoints(gray1, kp1, outImage=None)
image2 = cv2.drawKeypoints(gray2, kp2, outImage=None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(gray1, kp1, gray2, kp2, matches[:50], None)

cv2.imshow('sift1', image1)
cv2.imshow('sift2', image2)
plt.imshow(img3)
plt.show()
#cv2.imwrite('sift.jpg', image)

cv2.waitKey(2000)

