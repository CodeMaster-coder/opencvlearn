# 模板匹配
import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread(r'D:\\visiondetect\\xiangsuimg2.jpg')
    target = cv.imread(r'D:\\visiondetect\\image2.jpg')
    # target = target1[105:134,292:315]
    cv.namedWindow('template image', cv.WINDOW_NORMAL)
    cv.imshow("template image", tpl)
    cv.namedWindow('target image', cv.WINDOW_NORMAL)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED,cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_CCOEFF,cv.TM_CCOEFF_NORMED]  # 3种模板匹配方法
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(min_val, max_val)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)  # br是矩形右下角的点的坐标
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.namedWindow("match-" + str(md), cv.WINDOW_NORMAL)
        cv.imshow("match-" + str(md), target)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()