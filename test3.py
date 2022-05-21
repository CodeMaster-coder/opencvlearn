import cv2 as cv
import numpy as np


def blur_demo(image):
              # 均值模糊去随机噪声
              dst = cv.blur(image,(15,1))
              cv.imshow('blur_demo',dst)


def median_blur_demo(image):
    # 中值模糊去椒盐噪声
    dst = cv.medianBlur(image, 5)
    cv.imshow('median_blur_demo', dst)


def custom_blur_demo(image):
    # 自定义模糊
    # 防止溢出
    karnel = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(image,-1,kernel=karnel)
    # 中值模糊去椒盐噪声
    dst = cv.medianBlur(image, 5)
    cv.imshow('custom_blur_demo', dst)

image = cv.imread(r'D:\\visiondetect\\haibao.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
custom_blur_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()

