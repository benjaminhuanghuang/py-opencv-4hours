import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')

# display image as a new window
cv.imshow('Cats', img)
cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()