import numpy as np
import sys
import cv2
from filter import apply_filter
from filter import variance
from model import FaceKeypointsCaptureModel

rgb = cv2.VideoCapture(0)
fps = int(rgb.get(cv2.CAP_PROP_FPS))
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
labels = {}
countee=0

def __get_data__():


    _, fr = rgb.read()
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray, 1.3, 5)
    
    return faces, fr, gray

def start_app(cnn):
 

    countee=0
    ix = 0
    width  = int(rgb.get(3)) # float
    height = int(rgb.get(4))
   
    img1 = cv2.imread('final2.png')
    img1 = cv2.resize(img1, (1024, 768))   
    while True:
        ix += 1
        faces, fr, gray_fr = __get_data__()
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]   
            roi = cv2.resize(fc, (96, 96))
            pred, pred_dict = cnn.predict_points(roi[np.newaxis, :, :, np.newaxis])
            pred, pred_dict = cnn.scale_prediction((x, fc.shape[1]+x), (y, fc.shape[0]+y))

            hashe = apply_filter(faces, pred_dict)

        fr=cv2.resize(fr, (1024, 768))
        fin = cv2.addWeighted(fr,1.0,img1,0.1,0)
        cv2.imshow('Face Capture',fin)
 
        if cv2.waitKey(1)& 0xFF == ord('q'):
            variance()
            break

    rgb.release()
    cv2.destroyAllWindows()
    


if __name__ == '__main__':
    model = FaceKeypointsCaptureModel("face_model.json", "face_model.h5")
    start_app(model)