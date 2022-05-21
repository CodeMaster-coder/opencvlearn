import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(r'D:\\visiondetect\\haarcascades\\haarcascade_frontalface_default.xml')
eye_casecade = cv.CascadeClassifier(r'D:\\visiondetect\\haarcascades\\haarcascade_eye.xml')
camera = cv.VideoCapture(0)
while (True):
    ret,frame = camera.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for(x,y,w,h) in faces:
        image = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        eyes = eye_casecade.detectMultiScale(roi_gray, 1.03, 5, 0, (40,40))
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
            cv.imshow('camera',frame)
            c = cv.waitKey((50))
            if c == 27:
                break;




