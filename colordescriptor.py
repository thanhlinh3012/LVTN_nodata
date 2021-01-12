import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils

class ColorDescriptor:
    def __init__(self, bins):
        self.bins = bins                # bins: the number of bins for color histogram

    def describe(self, image):          
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert from the RGB color space to the HSV color space
        features = []

        (h, w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))     # center (x,y)

        # divide the img into 4 segments (top-left, top-right, bottom-right, bottom-left)
        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

        # elliptical mask representing the center of the img
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)      
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

        for (startX, endX, startY, endY) in segments:
            cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)

            # extract a color histogram from the image
            hist = self.histogram(image, cornerMask)
            features.extend(hist)
         # extract a color histogram from the elliptical region
        hist = self.histogram(image, ellipMask)
        features.extend(hist)       # update the feature vector
        return features

    def histogram(self, image, mask):
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])

        if imutils.is_cv2():        # for openCV 2.4
           hist = cv2.normalize(hist).flatten()
        else:                       # for openCV 3+
           hist = cv2.normalize(hist, hist).flatten()
        return hist


