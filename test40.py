import cv2
import numpy as np
import datetime as datetime


# 定义两个核	（kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
def detect(imgpath, b):
    kernel_Ero = np.ones((3, 1), np.uint8)
    kernel_Dia = np.ones((1, 3), np.uint8)
    img = cv2.imread(imgpath, 0)
    # 第一个区域检测
    copy_img1 = img[105:134, 292:315]
    dx = cv2.Sobel(copy_img1, -1, dx=1, dy=0, ksize=3)
    imgBlur1 = cv2.medianBlur(dx, 3)
    ret, thresh1 = cv2.threshold(imgBlur1, 127, 255, cv2.THRESH_BINARY)
    imgEro = cv2.erode(thresh1, kernel_Ero, iterations=3)
    imgDia = cv2.dilate(thresh1, kernel_Dia, iterations=3)
    contouts1, hie = cv2.findContours(imgDia, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt1 = contouts1
    a1 = []
    for i in cnt1:
        x, y, w, h = cv2.boundingRect(i)
        if w / h < 2.5:
            a1.append(i)
            cv2.drawContours(copy_img1, i, -1, (0, 255, 0), 2)
    print('最终检测到的轮廓数：%s' % (len(a1)))
    #             cv2.imwrite('/home/pi/visiondetect/detectedimg/section1/s1image%s.jpg' % b,copy_img1)
    #         else:
    #             cv2.imwrite('/home/pi/visiondetect/notdetectedimg/nsection1/ns1image%s.jpg' % b,copy_img1)

    # 第二个区域检测
    img2 = cv2.imread(imgpath)
    copy_img2 = img2[367:400, 260:290]
    lower_green = np.array([140, 140, 140])
    upper_green = np.array([255, 255, 255])
    imggreen2 = cv2.inRange(copy_img2, lower_green, upper_green)
    imgBlur2 = cv2.medianBlur(imggreen2, 3)
    ret, thresh2 = cv2.threshold(imgBlur2, 127, 255, cv2.THRESH_BINARY)
    imgEro2 = cv2.erode(thresh2, kernel_Ero, iterations=3)
    imgDia2 = cv2.dilate(thresh2, kernel_Dia, iterations=3)
    contouts2, hie = cv2.findContours(imgDia2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt2 = contouts2
    a2 = []
    # print('初步检测到的轮廓数：%s'%(len(cnt2)))
    # print(len(a))
    for j in cnt2:
        # 坐标赋值
        x, y, w, h = cv2.boundingRect(j)
        # print(w, h)
        # roi位置判断
        if w < h:
            # 画出轮廓
            # print(w, h)
            a2.append(j)
            cv2.drawContours(copy_img2, j, -1, (0, 255, 0), 2)
    #             cv2.imwrite('/home/pi/visiondetect/detectedimg/section2/s2image%s.jpg' % b,copy_img2)
    #         else:
    #             cv2.imwrite('/home/pi/visiondetect/notdetectedimg/nsection2/ns2image%s.jpg' % b,copy_img2)
    print('最终检测到的轮廓数：%s' % (len(a2)))
    cv2.imshow("copy_img1", copy_img1)
    cv2.imshow("copy_img2", copy_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(len(a2))
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(r'D:\\visiondetect\\recorder.txt','a') as f:
        f.write(time + '------' + '图像名：image%s' % b + '-----' + '区域1轮廓数：%s' % len(a1) + '-----' + '区域2轮廓数：%s \n' % len(a2))



    if len(a1) > 0 and len(a2) > 0:
        print('ok')
        # cv2.imwrite('/home/pi/visiondetect/shujuji/goodimg/image%s.jpg' % b, img2)
        return True

    else:
        print('nok')
        # cv2.imwrite('/home/pi/visiondetect/shujuji/badimg/image%s.jpg' % b, img2)
        return False

detect(r'D:\\visiondetect\\badimg\\image27.jpg',10)



