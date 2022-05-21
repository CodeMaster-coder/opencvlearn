import cv2
import numpy as np
from os.path import join


datapath = "D:\\visiondetect\\fapaojianimg"
def path(cls, i):
    return '%s\\%s%d.jpg' %(datapath,cls,i+1)

def extract_sift(fn):
    im = cv2.imread(fn, 0)
    return extract.compute(im, detect.detect(im))[1]

def bow_features(fn):
    im = cv2.imread(fn, 0)
    # print(extract_bow.compute(im, detect.detect(im)))
    return extract_bow.compute(im, detect.detect(im))

def predict(fn):
    f = bow_features(fn)

    p = svm.predict(f)
    # print (fn), '\t',p[1][0][0]
    return p
t1 = cv2.getTickCount()
pos, neg = 'pos-', 'neg-'

detect = cv2.xfeatures2d.SIFT_create()
extract = cv2.xfeatures2d.SIFT_create()

flann_params = dict(algorithm = 1, trees = 5)
flann = cv2.FlannBasedMatcher(flann_params, {})

bow_kmeans_trainer = cv2.BOWKMeansTrainer(45)
extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)



for i in range(8):
    bow_kmeans_trainer.add(extract_sift(path(pos, i)))

    bow_kmeans_trainer.add(extract_sift(path(neg, i)))

voc = bow_kmeans_trainer.cluster()
extract_bow.setVocabulary(voc)



traindata, trainlabels = [], []
for i in range(20):
    traindata.extend(bow_features(path(pos, i)))
    trainlabels.append(1)
    traindata.extend(bow_features(path(neg, i)))
    trainlabels.append(-1)
# print('f', traindata)

svm = cv2.ml.SVM_create()
svm.train(np.array(traindata), cv2.ml.ROW_SAMPLE,np.array(trainlabels))
svm.save('D:\\visiondetect\\svm.xml')



car = "D:\\visiondetect\\7.jpg"
car_img = cv2.imread(car)
car_predict = predict(car)


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


