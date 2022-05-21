import cv2 as cv
import numpy as np

def laplian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[1,1,1],[1, -8, 1],[1,1,1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel = kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('laplian_demo',lpls)



def sobel_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('gradian_x',gradx)
    cv.imshow('gradian_y',grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradient',gradxy)





image = cv.imread(r'D:\\visiondetect\\haibao.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
laplian_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()