import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('../Resources/Photos/cats.jpg')

# display image as a new window
cv.imshow('Cats', img)
cv.imshow('Resized Cats', rescaleFrame(img))
cv.waitKey(0) 


# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()