import cv2 as cv
import numpy as np


def bi_demo(image):
    x,y = image.shape[0:2]
    image1 = cv.resize(image,(int(x/3),int(y/2)))
    dst = cv.bilateralFilter(image1,0,50,7)
    cv.imshow('bi_demo',dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow('shift_demo',dst)

image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
shift_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()