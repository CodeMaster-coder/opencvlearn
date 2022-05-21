import cv2
import numpy as np
#定义两个核	（kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
kernel_Ero = np.ones((3,1),np.uint8)
kernel_Dia = np.ones((1,3),np.uint8)

# img = cv2.imread(r'D:\\visiondetect\\liwai\\image1.jpg')
img = cv2.imread(r'D:\\visiondetect\\badimg\\pos-13.jpg')
# copy_img = img[105:134,292:315]
copy_img = img[367:400, 260:290]
# copy_img = img
#HSV转换
imgHSV = cv2.cvtColor(copy_img,cv2.COLOR_RGB2HSV)
# imgHSV = cv2.cvtColor(copy_img,cv2.COLOR_BGR2GRAY)
#绿色提取
# lower_green = np.array([78,51,46])
# upper_green = np.array([79, 64, 255])
lower_green = np.array([35,43,46])
upper_green = np.array([77, 255, 255])
imggreen  = cv2.inRange(imgHSV, lower_green, upper_green)
# dx = cv2.Sobel(copy_img,-1,dx =1,dy = 0,ksize=1)
# dx = cv2.Laplacian(copy_img,-1 ,ksize=5)
# dx = cv2.Scharr(copy_img,-1,dx = 1,dy = 0)
# dx = cv2.Sobel(copy_img,-1,dx = 0,dy = 1,ksize=3)
#高斯滤波去噪
# imgBlur = cv2.GaussianBlur(imggreen,(3,3),1)
# imgBlur = cv2.bilateralFilter(imggreen,8,10,50)
imgBlur = cv2.medianBlur(imggreen, 5)
# imgBlur = cv2.fastNlMeansDenoisingColored(imggreen, None, 15, 15, 10, 30)
# #阈值处理
ret,thresh = cv2.threshold(imggreen,127,255,cv2.THRESH_BINARY)
# #腐蚀
imgEro = cv2.erode(thresh,kernel_Ero,iterations=3)
# kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# imgEro = cv2.filter2D(imgBlur, -1 ,kernel)
# # #膨胀
imgDia = cv2.dilate(thresh,kernel_Dia,iterations=3)

# #轮廓检测
contouts,hie = cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = contouts
print('初步检测到的轮廓数：%s'%(len(cnt)))

a = []
for i in cnt:
    #坐标赋值
    x,y,w,h = cv2.boundingRect(i)
    print(w, h)
    #roi位置判断

    if   w<h:
        # 画出轮廓
        print(w, h)
        a.append(i)
        cv2.drawContours(copy_img, i, -1, (0, 255, 0), 2)
print('最终检测到的轮廓数：%s' % (len(a)))

cv2.imshow("img",copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
