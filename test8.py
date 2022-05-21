import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt

def back_projection_demo():
    image1 = cv.imread(r'D:\\visiondetect\\sample1.png')
    image2 = cv.imread(r'D:\\visiondetect\\smarties.png')
    image1_hsv = cv.cvtColor(image1,cv.COLOR_RGB2HSV)
    image2_hsv = cv.cvtColor(image2, cv.COLOR_RGB2HSV)

    cv.imshow('image1',image1)
    cv.imshow('image2', image2)


    image1Hist = cv.calcHist([image1_hsv],[0,1],None,[36,36],[0,180,0,256])
    cv.normalize(image1Hist,image1Hist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([image2_hsv],[0,1],image1Hist,[0,180,0,256],1)
    cv.imshow('backprojectiondemo',dst)
def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_RGB2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,250])
    # cv.imshow('hist2d',hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title('2d histogram')
    plt.show()


image = cv.imread(r'D:\\visiondetect\\haibao.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
back_projection_demo()
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()