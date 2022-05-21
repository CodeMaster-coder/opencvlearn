import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow('add_demo',dst)


def sub_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow('sub_demo',dst)

def div_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('div_demo', dst)

def mul_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('mul_demo', dst)

def logic_demo(m2):
    dst = cv.bitwise_not(m2)
    cv.imshow('logic_demo',dst)

def others(m1,m2):
    main1,dev1 = cv.meanStdDev(m1)
    main2,dev2 = cv.meanStdDev(m2)
    print(main1)
    print(main2)
    print(dev1)
    print(dev2)

image1 = cv.imread(r'D:\\visiondetect\\LinuxLogo.jpg')
image2 = cv.imread(r'D:\\visiondetect\\WindowsLogo.jpg')
print(image1.size)
print(image2.size)
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('image1', image1)
cv.imshow('image2', image2)
# 计算代码执行速度
t1 = cv.getTickCount()
# get_image_info(image)
# access_pixels(image)
# creat_image()
# color_space_demo(image)
# add_demo(image1,image2)
# sub_demo(image1,image2)
# div_demo(image1,image2)
# mul_demo(image1,image2)
# others(image1,image2)
logic_demo(image2)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))

cv.waitKey(0)
cv.destroyAllWindows()