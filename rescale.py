import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works for imnages, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Works for live video only
    capture.set(3.width)
    capture.set(4,height)

img = cv.imread('Photos/cat_large.jpg')
img_resize = rescaleFrame(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', img_resize)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()