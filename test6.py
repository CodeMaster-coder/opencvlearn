import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    # 亮度直方图
    plt.hist(image.ravel(),256,[0,256])
    plt.show('plot_demo')

def image_hist(image):
    # 色彩直方图
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color = color)
        plt.xlim([0,256])
    plt.show()


image = cv.imread(r'D:\\visiondetect\\haibao.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
image_hist(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()