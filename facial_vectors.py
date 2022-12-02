#https://blog.csdn.net/weixin_46628481/article/details/121108706
import numpy as np
import cv2
import dlib
import os
import sys
import random
import time
import hashkey_gen
from reedsolo import RSCodec

#output_dir stores the output of the
output_dir = './faces'
size = 64

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# change the contrust and brightness

def relight(img, light=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]
    #image = []
    for i in range(0,w):
        for j in range(0,h):
            for c in range(3):
                tmp = int(img[j,i,c]*light + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j,i,c] = tmp
    return img

#use dlib.frontal_face_detector as our feature exrtactor
detector = dlib.get_frontal_face_detector()

#camera = cv2.VideoCapture('path of mp4 file')
ok = True
is_camera = True
#is_camera = False means read pictures instead of live capture

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')



def process_img(img,detector,predictor):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rects = detector(img_gray, 0)

    last_list = np.array([])
    sample_list = []

    for i in range(len(rects)):

        sample_list = []

        landmarks = np.matrix([[p.x, p.y] for p in predictor(img,rects[i]).parts()])
        for idx, point in enumerate(landmarks):
            # pos is the coordinate of each point
            pos = (point[0, 0], point[0, 1])
            sample_list.append(pos)
            #print(idx,pos)

            # circle all 68 data points
            cv2.circle(img, pos, 2, color=(0, 255, 0))
            # label all those points
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(idx+1), pos, font, 0.2, (0, 0, 255), 1,cv2.LINE_AA)
    cv2.imshow('video', img)
    feature_list = np.array([])
    if len(sample_list)==68:
        feature_list = hashkey_gen.feature_cal(sample_list)


    return feature_list


if is_camera == True:

    rsc = RSCodec(10)
    camera = cv2.VideoCapture(0)
    last_feature = np.array([])
    feature_avg = np.array([])
    flag = 0
    stable_flage = 0

    while ok:
        # if ok, live capture is normal
        ok, img = camera.read()

        # convert image to grayscale
        feature_list = process_img(img,detector,predictor)
        feature_list = feature_list*100

        if flag<5: #take the average of 20 capture
            if len(feature_avg)==0:
                feature_avg = feature_list.astype(int)
                flag+=1
            else:
                feature_avg = feature_avg+feature_list
                flag+=1

        else:
            flag = 0

            feature_avg = feature_avg/5
            #np.ceil(feature_avg)

            if len(last_feature)!=0:
                #print(last_feature-feature_avg)#print the variance compare to the last feature_avg
                pass
            last_feature = feature_avg

            arr = feature_avg.astype(int)
            feature_avg_list = arr.tolist()
            feature_str = ''.join(str(num) for num in feature_avg_list)
            feature_byte = bytes(feature_str,'utf-8')
            #print(rsc.encode(feature_byte))
            print(feature_str)

        k = cv2.waitKey(1)
        if k == 27:    # press 'ESC' to quit
            break

    camera.release()
    cv2.destroyAllWindows()

else:

    for i in range (0,10):
        img = cv2.imread('./img2/'+str(i+1)+'.jpeg')
        feature_list = (process_img(img,detector,predictor)*100).astype(int)
        feature_avg_list = feature_list.tolist()
        feature_str = ''.join(str(num) for num in feature_avg_list)
        print(feature_str)

        k = cv2.waitKey(1)

        time.sleep(1)
