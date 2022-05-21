import cv2
import numpy as np
img = cv2.imread(r'D:\\visiondetect\\badimg\\neg-1.jpg')
husky = img[92:163,272:338]
# imgHSV = cv2.cvtColor(husky,cv2.COLOR_RGB2HSV)
# imgHSB = cv2.cvtColor(img,cv2.COLOR_RGB2HSB)
# print(imgHSB[9,6])
# husky = img[325:445, 200:340]
# img[61:300,270:480] = husky
# cv2.imshow("img",husky)
cv2.imwrite(r'D:\\visiondetect\\xiangsuimg4.jpg',husky)
# cv2.imshow("img1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()