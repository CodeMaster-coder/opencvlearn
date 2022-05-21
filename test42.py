import os
from test41 import *
import cv2

# 获取当前目录下所有文件名并返回一个列表
path = 'D:\\shujuji'
filelist = os.listdir(path)
for i in filelist:
    imgpath = 'D:\\shujuji\\' + i
    print(i)
    img2 = cv2.imread(imgpath)
    SIG = detect(imgpath,i)
    if SIG:
        cv2.imwrite(r'D:\\GOOD\\' + i, img2)
    else:
        cv2.imwrite(r'D:\\BAD\\' + i, img2)