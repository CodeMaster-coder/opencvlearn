import cv2 as cv
import numpy as np


def get_image_info(image):
    print(image.shape)
    print(image.size)
    print(image.dtype)
    print(type(image))
    pixel_data = np.array(image)
    print(pixel_data)



def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        cv.flip(frame,1)
        cv.imshow('video',frame)
        c = cv.waitKey((50))
        if c == 27:
            break;


# 遍历像素点，像素取反
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('width : %s,height : %s,chnnels : %s'%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255-pv
    cv.imshow('pixels_demo',image)

def creat_image():
# 多通道赋值
    # img = np.zeros([400,400,3],np.uint8)
    # img[:,:,0] = np.ones([400,400])*255
    # cv.imshow('newimage',img)
#     单通道赋值
    img = np.zeros([400, 400,1], np.uint8)
    img[:,:,0] = np.ones([400,400]) * 127
    cv.imshow('new image',img)
    cv.imwrite(r'D:\\visiondetect\\myimage.png',img)


def inverse(image):
    # 像素取反API
    dst = cv.bitwise_not(image)
    cv.imshow('inverse demo',dst)



image = cv.imread(r'D:\\visiondetect\\haibao.jpg')
h,w = image.shape[:2]
cX,cY = (w//4,h//4)
image[0:cY,0:cX] = (0,0,255)
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', image)
# 计算代码执行速度
t1 = cv.getTickCount()
# get_image_info(image)
# access_pixels(image)
# creat_image()
inverse(image)
t2 = cv.getTickCount()
print('time:%s ms'%((t2-t1)/cv.getTickFrequency()*1000))
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()

# #获取图片高度，宽度，颜色通道数
# (h,w,c) = image.shape
# print(image.shape)
#
# #获取第一个像素点
# (b,g,c) = image[0,0]
# print(image[0,0])
#
# #修改第一个像素点颜色为红色
# image[0,0] = (0,0,255)
# (b,g,c) = image[0,0]
# print(image[0,0])




