import cv2
import numpy as np
from matplotlib import pyplot as plt

dst1 = cv2.imread(r'D:\\visiondetect\\image1.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.GaussianBlur(dst1,(3,3),0)
dst2 = cv2.imread(r'D:\\visiondetect\\xiangsuimg1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.GaussianBlur(dst2,(3,3),0)
orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
matches = bf.match(des1,des2)
matches = sorted(matches,key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:40],img2,flags=2)
plt.imshow(img3),plt.show()
while(True):
    cv2.imshow('sift_keypoints',dst1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





