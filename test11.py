import cv2 as cv
import numpy as np



def big_image_demo(image):
    # 超大图像二值化
    print(image.shape)
    cw = 256
    ch =256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 157, 20)
            gray[row:row+ch,col:col+cw] = dst
            print(np.std(dst),np.mean(dst))
    cv.imwrite(r'D:\\visiondetect\\result_binary.jpg',gray)
image = cv.imread(r'D:\\visiondetect\\mouse.jpg')

# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
big_image_demo(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()