import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(510,55),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    # 从(510,55)这个像素点出发，找到周围所有在(100,100,100)和(50,50,50)之间的值点，填充颜色(0,255,255)
    cv.imshow('fill_color_demo',copyImg)


def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow('fill_binary',image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    # floodfill填充式mask区域必须为0，否则不工作
    cv.imshow('fill_binary1', image)


image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', image)
print(image.shape)
face = image[120:550,100:550]

grey = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(grey,cv.COLOR_GRAY2BGR)
image[120:550,100:550] = backface

cv.imshow('image',image)
# 计算代码执行速度
t1 = cv.getTickCount()
# fill_color_demo(image)
fill_binary()
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))

cv.waitKey(0)
cv.destroyAllWindows()