import cv2
import numpy as np
import datetime as datetime
import time


# 定义两个核	（kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
def detect(imgpath,b):

    kernel_Ero = np.ones((1, 3), np.uint8)
    kernel_Dia1 = np.ones((1, 3), np.uint8)
    kernel_Dia2 = np.ones((3, 1), np.uint8)
    img = cv2.imread(imgpath,0)
    img1 = cv2.imread(imgpath)
    # img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    # 第一个区域检测
    copy_img1 = img[105:130, 292:315]
    # dx = cv2.Sobel(copy_img1, -1, dx=1, dy=0, ksize=3)
    # imgBlur1 = cv2.medianBlur(dx, 3)
    ret, thresh3 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    ret, thresh1 = cv2.threshold(copy_img1, 180, 255, cv2.THRESH_BINARY)


    copYIMG1 = cv2.resize(thresh1,None,fx=5,fy=5)
    cv2.imshow("img", thresh3)
    cv2.imshow("copy_img0", thresh1)
    # cv2.imshow("copy_img2", copy_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





detect('D:\\visiondetect\\fapaojianlishishuju\\badimg\\image1557.jpg','image1.jpg')



