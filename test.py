import cv2 as cv
import numpy as np

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    hsv = cv.cvtColor(image,cv.COLOR_RGB2HSV)
    cv.imshow('hsv',hsv)
    yuv = cv.cvtColor(image,cv.COLOR_RGB2YUV)
    cv.imshow('yuv',yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow('ycrcb',ycrcb) 


def extract_object_demo():
    # 色彩提取绿色
    capture = cv.VideoCapture(r'D:\\visiondetect\\video.mp4')
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow('video', frame)
        cv.imshow('mask',mask)
        c = cv.waitKey(40)
        if c == 27:
            break;




image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
# get_image_info(image)
# access_pixels(image)
# creat_image()
# color_space_demo(image)
extract_object_demo()
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))

cv.waitKey(0)
cv.destroyAllWindows()