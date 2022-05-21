import cv2 as cv
import numpy as np
pic_len = 512

img_file = r"D:\\visiondetect\\14.jpg"


a = cv.imread(r"D:\\visiondetect\\14.jpg")  # 读取图像


l, w, h = a.shape  # 获取图像的属性
# print(str(i)+"= ",a.shape)
# cv.imshow("Original "+str(i),a)
if l >= w:  # 初步放缩，以防图像大但兴趣域小的情况出现
    size = (round((pic_len / l) * w), pic_len)
else:
    size = (pic_len, round((pic_len / w) * l))
a = cv.resize(a, size)
l, w, h = a.shape
# print("after "+str(i)+'= ',a.shape)
# cv.imshow("After "+str(i),a)

# 将图片调整为方形的图片
s = np.ones((pic_len, pic_len, 3), dtype=np.uint8) * 255
if l <= pic_len and w <= pic_len:
    s[((pic_len - l) // 2):(l + (pic_len - l) // 2), ((pic_len - w) // 2):(w + (pic_len - w) // 2), :] = a[:, :, :]
elif l > pic_len and w <= pic_len:
    s[:, ((pic_len - w) // 2):(w + (pic_len - w) // 2), :] = a[((l - pic_len) // 2):(pic_len + (l - pic_len) // 2),
                                                             :, :]
elif l <= pic_len and w > pic_len:
    s[((pic_len - l) // 2):(l + (pic_len - l) // 2), :, :] = a[:,
                                                             ((w - pic_len) // 2):(pic_len + (w - pic_len) // 2), :]
elif l > pic_len and w > pic_len:
    s[:, :, :] = a[((l - pic_len) // 2):(pic_len + (l - pic_len) // 2),
                 ((w - pic_len) // 2):(pic_len + (w - pic_len) // 2), :]
# cv.imshow("s"+str(i),s)
# cv.imwrite("bana-"+str(i)+".jpg",s)

# 第二次放缩，得到最终的图片
size = (800, 800)
c = cv.resize(s, size)

cv.imwrite(img_file + 'neg-%d.jpg', c) #256*256大小的图片


