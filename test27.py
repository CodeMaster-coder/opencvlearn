import cv2
import numpy as np
from matplotlib import pyplot as plt


dst1 = cv2.imread(r'D:\\visiondetect\\image1.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.GaussianBlur(dst1,(3,3),0)
dst2 = cv2.imread(r'D:\\visiondetect\\cutimg1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.GaussianBlur(dst2,(3,3),0)

sift = cv2.xfeatures2d.SIFT_create()
# 查找监测点和匹配符
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# print(len(kp1), len(des1))  # 1402, 1402

FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
searchParams = dict(checks=50)
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
# 进行匹配
matches = flann.knnMatch(des1, des2, k=2)
# 准备空的掩膜 画好的匹配项
matchesMask = [[0, 0] for i in range(len(matches))]

good = []
for i, (m, n) in enumerate(matches):
    if m.distance < 0.3 * n.distance:
        matchesMask[i] = [1, 0]
        good.append(m)
print(len(good))
drawPrams = dict(matchColor=(0, 255, 0),
                 singlePointColor=(255, 0, 0),
                 matchesMask=matchesMask,
                 flags=0)
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **drawPrams)
img_PutText = cv2.putText(img3, "SIFT+kNNMatch: Image Similarity Comparisonn", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1.5,
                          (0, 0, 255), 3, )
img4 = cv2.resize(img_PutText, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)  # 缩小1/2

cv2.imshow("matches", img4)
cv2.waitKey()
cv2.destroyAllWindows()