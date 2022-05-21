import cv2 as cv
import numpy as np

def threshhold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print('threshhold value %s'%ret)
    cv.imshow('binary',binary)

def local_threshhold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)

    cv.imshow('binary',dst)

def custome_threshhold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray,[1,w*h])
    mean = m.sum() / (w*h)
    print('mean:',mean)
    ret,dst = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)

    cv.imshow('binary',dst)





image = cv.imread(r'D:\\visiondetect\\haibao.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
custome_threshhold(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()