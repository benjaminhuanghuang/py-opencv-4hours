
import cv2 as cv
import numpy as np



img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

average = cv.blur(img, (8,8))
cv.imshow('Average', average)

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss', gauss)

median = cv.medianBlur(img, 3)
cv.imshow('Median', median)


bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
