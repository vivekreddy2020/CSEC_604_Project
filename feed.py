import numpy as np
import sys
import cv2
from filter import capture
from filter import variance
from model import FaceKeypointsCaptureModel
import time

rgb = cv2.VideoCapture(0)

fps = int(rgb.get(cv2.CAP_PROP_FPS))
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cnn = FaceKeypointsCaptureModel("face_model.json", "face_model.h5")


def __get_data__():
    try:
        _, fr = rgb.read()
        gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray, 1.3, 5)
    
        return faces, fr, gray
    except:
        sys.exit("Program terminated!!")
        return 0


def start_app():
    feature = ''
    timedout = int(5)
    width  = int(rgb.get(3))
    height = int(rgb.get(4))
    flag=0
    img1 = cv2.imread('template.png')
    img1 = cv2.resize(img1, (1024, 768))   
    while True:
        faces, fr, gray_fr = __get_data__()
        if cv2.waitKey(1)& 0xFF == ord('c'):
            flag = int(1)  
            timedout= timedout+int(time.perf_counter())
        
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]   
            roi = cv2.resize(fc, (96, 96))
            pred, pred_dict = cnn.predict_points(roi[np.newaxis, :, :, np.newaxis])
            pred, pred_dict = cnn.scale_prediction((x, fc.shape[1]+x), (y, fc.shape[0]+y))

            if flag == 1:
                if capture(faces, pred_dict):
                    print("capturing.....")
        fr=cv2.resize(fr, (1024, 768))
        fin = cv2.addWeighted(fr,1.0,img1,0.1,0)
        cv2.imshow('Face Capture',fin)
   
        if timedout == int(time.perf_counter()):
            feature = variance()
            cv2.destroyWindow('Face Capture')
            rgb.release()
            break
        
    return feature
    