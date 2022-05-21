import cv2 as cv
import numpy as np

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
#     X gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
#     Y gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
#     edge
    edge_output = cv.Canny(xgrad,ygrad,50,150)
    cv.imshow('canny edge',edge_output)
    dst = cv.bitwise_and(image,image,mask = edge_output)
    cv.imshow('color edge',dst)



image = cv.imread(r'D:\\visiondetect\\lena.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
edge_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()