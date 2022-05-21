import cv2 as cv
import numpy as np


def contours_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    # 高斯去噪声
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    # 取得灰度图
    ret,binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # 图像二值化
    cv.imshow('binary image',binary)

    contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE,  )
    # 找到轮廓
    for i,contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0,0,255), 2)
        # cv.drawContours(image, contours, i, (0, 0, 255), -1) 填充所有轮廓
        print(i)
    cv.imshow('detect_contours',image)


image = cv.imread(r'D:\\visiondetect\\coins.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
contours_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()