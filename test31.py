import cv2
import numpy as np
import os
from os.path import join
import joblib
import sys
# path='C:\\Users\\liuke\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\libsvm\\'
# sys.path.append(path)

# from svmutil import *
# from sklearn import svm


# datapath = "D:\\visiondetect\\fapaojianimg"
# def path(cls, i):
#     return '%s\\%s%d.jpg' %(datapath,cls,i+1)
t1 = cv2.getTickCount()
pos, neg = 'pos-', 'neg-'

detect = cv2.xfeatures2d.SIFT_create()
extract = cv2.xfeatures2d.SIFT_create()

flann_params = dict(algorithm = 1, trees = 5)
flann = cv2.FlannBasedMatcher(flann_params, {})

bow_kmeans_trainer = cv2.BOWKMeansTrainer(45)
extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)



# for i in range(8):
#     bow_kmeans_trainer.add(extract.compute(cv2.imread(path(pos, i), 0), detect.detect(cv2.imread(path(pos, i), 0)))[1])
#     bow_kmeans_trainer.add(extract.compute(cv2.imread(path(neg, i), 0), detect.detect(cv2.imread(path(neg, i), 0)))[1])
#
# voc = bow_kmeans_trainer.cluster()
# np.save('D:\\visiondetect\\voc.npy',voc)
voc = np.load('D:\\visiondetect\\voc.npy')
extract_bow.setVocabulary(voc)
# print(type(voc), voc.shape)



# traindata, trainlabels = [], []
# for i in range(20):
#     traindata.extend(extract_bow.compute(cv2.imread(path(pos, i), 0), detect.detect(cv2.imread(path(pos, i), 0))))
#     trainlabels.append(1)
#     traindata.extend(extract_bow.compute(cv2.imread(path(neg, i), 0), detect.detect(cv2.imread(path(neg, i), 0))))
#     trainlabels.append(-1)
# print(np.array(traindata), trainlabels)
svm = cv2.ml.SVM_create()
# svm1 = svm.train(np.array(traindata), cv2.ml.ROW_SAMPLE,np.array(trainlabels))
# joblib.dump(filename='LR.model',value=svm1)
# joblib.load(filename="LR.model")
# svm.save('D:\\visiondetect\\svm1.xml')
svm = svm.load('D:\\visiondetect\\svm.xml')




car = "D:\\visiondetect\\image6.jpg"
car_img = cv2.imread(car)
car_predict = svm.predict(extract_bow.compute(cv2.imread(car, 0), detect.detect(cv2.imread(car, 0))))

font = cv2.FONT_HERSHEY_SIMPLEX

if (car_predict[1][0][0] == 1.0):
    print(car_predict)
    cv2.putText(car_img,'detected',(10,30),font,1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('bow + svm success', car_img)
    t2 = cv2.getTickCount()
    print('time:%s s' % ((t2 - t1) / cv2.getTickFrequency()))
    cv2.waitKey()
    cv2.destroyAllWindows()

if (car_predict[1][0][0] == -1.0):
    cv2.putText(car_img,'not detected',(10,30),font,1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('now + svm failure', car_img)
    t2 = cv2.getTickCount()
    print('time:%s s' % ((t2 - t1) / cv2.getTickFrequency()))
    cv2.waitKey()
    cv2.destroyAllWindows()


