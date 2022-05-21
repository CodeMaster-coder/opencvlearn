import cv2 as cv
import numpy as np
import sys as sys


imgpath = sys.argv[1]
img = cv.imread(imgpath)
alg = sys.argv[2]

def fd(algorithm):
    if algorithm == 'SIFT':
        return cv.xfeatures2d.SIFT_create()
    if algorithm =='SURF':
        return  cv.xfeatures2d.SURF_create(float(sys.argv[3]) if len(sys.argv) == 4 else 4000)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
fd_alg = fd(alg)

keypoints, descripyor = fd_alg.detectAndCompute(gray,None)
img = cv.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,color=(51,163,236))
while(True):
    cv.imshow('sift_keypoints',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

