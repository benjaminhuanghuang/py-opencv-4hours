import cv2 as cv
import numpy as np

blankImg = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blankImg.copy(), (30, 30), (370, 370), 255, thickness=-1)
circle = cv.circle(blankImg.copy(), (200, 200), 200, 255, thickness=-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

bitwize_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwize_and)

bitwize_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwize_or)

bitwize_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwize_xor)

bitwize_not = cv.bitwise_not(circle)
cv.imshow('XOR', bitwize_not)

cv.waitKey(0)
