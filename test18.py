import cv2 as cv
import numpy as np

def measure_object(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('threshold value : %s'%ret)
    cv.imshow('binary image',binary)
    binimage = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x,y,w,h = cv.boundingRect(contour)
        rate = min(w,h)/max(w,h)
        print('rectangle rate: %s'%rate)
        mm = cv.moments(contour)
        type(mm)
        if mm['m00']:
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
        else:
            continue
        cv.circle(binimage, (np.int_(cx),np.int_(cy)), 2, (0,255,255), -1)
        cv.rectangle(binimage, (x,y), (x+w, y+h), (0,0,255), 2)
        approxCurve = cv.approxPolyDP(contour, 4, True)
        print(approxCurve.shape)
        if approxCurve.shape[0] > 10:
            cv.drawContours(binimage, contours, i, (0,255,0), 2)
        cv.imshow('measure-contour',binimage)






image = cv.imread(r'D:\\visiondetect\\shapes.jpeg')

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
measure_object(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()