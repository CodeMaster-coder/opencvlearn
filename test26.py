import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 25
dst1 = cv2.imread(r'D:\\visiondetect\\\\badimg\\pos-1.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.GaussianBlur(dst1,(3,3),0)
dst2 = cv2.imread(r'D:\\visiondetect\\xiangsuimg1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.GaussianBlur(dst2,(3,3),0)

sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k = 2)

good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

    M,mask = cv2.findHomography(src_pts, dst_pts,cv2.RANSAC,5,0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([[0,0], [0,h-1], [w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3,cv2.LINE_AA)
    print(len(good))
    print('similarity value:%s' %(MIN_MATCH_COUNT/len(good)))
else:
    print ("not enough matches are found %d/%d" %(len(good),MIN_MATCH_COUNT))
    matchesMask = None
draw_params = dict(matchColor = (0,255,0),  matchesMask = matchesMask,flags = 2)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
plt.imshow(img3,'gray'),plt.show()