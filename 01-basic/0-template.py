import cv2 as cv
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Cats', img)

blankImg = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blankImg)

cv.waitKey(0)