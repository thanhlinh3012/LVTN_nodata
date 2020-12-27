import cv2
import numpy as np
import glob
import argparse
import csv
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True)
ap.add_argument("-d", "--dataset", required=True)
args = vars(ap.parse_args())


im_shape = (300, 300)

image1 = cv2.imread(args["index"])
#image2 = cv2.imread('queries\q6b.jpg')

img1_resized = cv2.resize(image1, im_shape)
#img2_resized = cv2.resize(image2, im_shape)

cv2.imshow('img1', img1_resized)
#cv2.imshow('img2', img2_resized)
gray1 = cv2.cvtColor(img1_resized, cv2.COLOR_BGR2GRAY)
#gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
#kp2, des2 = sift.detectAndCompute(gray2, None)

image1 = cv2.drawKeypoints(gray1, kp1, outImage=None)
#image2 = cv2.drawKeypoints(gray2, kp2, outImage=None)


index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

results = {}
img_compare = []
titles = []
output = open("similarity.csv", "w")
for f in glob.iglob(args["dataset"] + "/*"):
    image = cv2.imread(f)
    img2_resized = cv2.resize(image, im_shape)
    gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)
    titles.append(f)
    img_compare.append(gray2)

for img_cmp, title in zip(img_compare, titles):
    if image1.shape == img_cmp.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(image1, img_cmp)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100% (equal size and channels)")
            break
        # 2) Check for similarities between the 2 images
    kp2, des2 = sift.detectAndCompute(img_cmp, None)
    matches = flann.knnMatch(des1, des2, k=2)
    good_points = []
    ratio_thresh = 0.7
    for m, n in matches:
        if m.distance < ratio_thresh * n.distance:
            good_points.append(m)
    number_keypoints = 0
    if len(kp1) >= len(kp2):
        number_keypoints = len(kp1)
    else:
        number_keypoints = len(kp2)
    print("Title: " + title)
    print("kp1:", len(kp1))
    print("kp2:", len(kp2))
    print("gp:", len(good_points))
    percentage_similarity = float(len(good_points) / number_keypoints * 100)
    per_sorted = sorted(percentage_similarity)
    output.write("%s\n" % (str(per_sorted)))
    #sorted(percentage_similarity)
    print("Similarity: " + str(int(percentage_similarity)) + "\n")

#results = sorted([(v, k) for (k, v) in results.items()])
#bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

#matches = bf.match(des1, des2)
#matches = sorted(matches, key = lambda x:x.distance)

#img3 = cv2.drawMatches(gray1, kp1, gray2, kp2, matches, None)

#cv2.imshow('sift1', img3)
#cv2.imshow('sift2', image2)
#plt.imshow(img3)
plt.show()
#cv2.imwrite('sift.jpg', image)

cv2.waitKey(60000)

