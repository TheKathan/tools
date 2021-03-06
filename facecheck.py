import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

img1 = cv2.imread(sys.argv[1],0)
img2 = cv2.imread(sys.argv[2],0) # trainImage

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

if len(good) > 2:
    print '1'
else:
    print '0'
