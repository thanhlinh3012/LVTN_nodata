import cv2
import numpy as np
import argparse

class SIFTDescriptor:
    def describe(self):
        image = cv2.imread('queries\q1.jpg')
        cv2.imshow('img', image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        kp = sift.detect(gray, None)

        image = cv2.drawKeypoints(gray, kp, outImage = None)

        #cv2.imwrite('sift.jpg', image)
        cv2.imshow('sift', image)
        cv2.waitKey(2000)

