import cv2 as cv
import numpy as np


image = cv.imread(r'D:\\visiondetect\\blox.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 23, 0.04)
image[dst > 0.01 * dst.max()] = [0,0,255]
while(True):
    cv.imshow('corner', image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', image)
# # 计算代码执行速度
# t1 = cv.getTickCount()
#
# t2 = cv.getTickCount()
# print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# # video_demo()
# cv.waitKey(0)
# cv.destroyAllWindows()