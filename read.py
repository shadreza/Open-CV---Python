import cv2 as cv

# to show an image on a particular path

# img = cv.imread('./Images/cow.jpg')
# cv.imshow('Cow', img)

# as the image size is far bigger so this has to be fixed ...

# this is a like a key needs to be pressed and the witing time is infinite
# cv.waitKey(0)


# now comming to video

# in cv.VideoCapture() the argument is like if you give a video file path then you are working with that particular video. But if 0 then its normally the webcam of the device. If 1 then its the 1st added external camera and then it goes like n means nth externally added camera
capture = cv.VideoCapture('./Videos/cars-moving.mp4')

# while the key 'd' is not pressed then it will run the loop. In each loop it is reading a frame and then making it up and showing the video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# after the video is shown the capture program should be released and all the working window needs to be destroyed
capture.release()
cv.destroyAllWindows()
