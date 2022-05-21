import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread(r'D:\\visiondetect\\nose.png')
    target = cv.imread(r'D:\\visiondetect\\baboon.jpg')
    cv.imshow('template_image',tpl)
    cv.imshow('target_image',target)
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.imshow('match_'+np.str_(md),target)


# image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
#
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
template_demo()
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()