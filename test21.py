import cv2 as cv
import numpy as np


face_cascade = cv.CascadeClassifier(r'D:\\visiondetect\\haarcascades\\haarcascade_frontalface_default.xml')
image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
    image = cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()

t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()