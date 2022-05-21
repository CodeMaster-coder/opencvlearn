import cv2 as cv
import numpy as np

def equalHist_demo(image):
    # 直方图均衡化，自动图像增强手段
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equal_demo',dst)

def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow('clahe_demo', dst)


def create_rgb_hist(image):
    # 色彩直方图原理代码
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    # 把256*256*256的图降维到16*16*16
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int_(b/bsize)*16*16 + np.int_(g/bsize)*16 + np.int_(r/bsize)
            rgbHist[np.int_(index),0] = rgbHist[np.int_(index),0] + 1
    return  rgbHist


def hist_compare(image1,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    # 巴氏距离
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
#     相关性比较
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
#     卡方比较越大越不相似
    print('巴氏距离: %s,相关性: %s,卡方: %s'%(match1,match2,match3))



image1 = cv.imread(r'D:\\visiondetect\\Blender_Suzanne1.jpg')
image2 = cv.imread(r'D:\\visiondetect\\Blender_Suzanne2.jpg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('image1', image1)
cv.imshow('image2', image2)
# 计算代码执行速度
t1 = cv.getTickCount()
hist_compare(image1,image2)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()