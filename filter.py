import hashlib
import statistics
from statistics import mode

import cv2
import numpy as np

import cryptic
from model import FaceKeypointsCaptureModel

eyelength=[]
eyelength_var=[]
facelength=[]
facelength_var=[]
faceheight=[]
faceheight_var=[]
eyebrowdistance=[]
eyebrowdistance_var=[]
mouthheight=[]
mouthheight_var=[]
mouthlength=[]
mouthlength_var=[]

def capture(frame, pts_dict):

    left_eye_center_x = pts_dict["left_eye_center_x"]
    left_eye_center_y = pts_dict["left_eye_center_y"]
    left_eye_inner_corner_x = pts_dict["left_eye_inner_corner_x"]
    left_eye_inner_corner_y = pts_dict["left_eye_inner_corner_y"]
    left_eye_outer_corner_x = pts_dict["left_eye_outer_corner_x"]
    left_eye_outer_corner_y = pts_dict["left_eye_outer_corner_y"]
    left_eyebrow_outer_end_x = pts_dict["left_eyebrow_outer_end_x"]
    left_eyebrow_outer_end_y = pts_dict["left_eyebrow_outer_end_y"]
    radius_left = distance2((left_eye_center_x, left_eye_center_y),
                           (left_eye_inner_corner_x, left_eye_inner_corner_y))

    right_eye_center_x = pts_dict["right_eye_center_x"]
    right_eye_center_y = pts_dict["right_eye_center_y"]
    right_eye_outer_corner_x = pts_dict["right_eye_outer_corner_x"]
    right_eye_outer_corner_y = pts_dict["right_eye_outer_corner_y"]
    right_eye_inner_corner_x = pts_dict["right_eye_inner_corner_x"]
    right_eye_inner_corner_y = pts_dict["right_eye_inner_corner_y"]
    right_eyebrow_outer_end_x = pts_dict["right_eyebrow_outer_end_x"]
    right_eyebrow_outer_end_y = pts_dict["right_eyebrow_outer_end_y"]
    radius_right = distance2((right_eye_center_x, right_eye_center_y),
                           (right_eye_inner_corner_x, right_eye_inner_corner_y))
    
    radius_eyes = distance2((right_eye_center_x, right_eye_center_y),
                           (right_eyebrow_outer_end_x, right_eyebrow_outer_end_y))
    
    length_eyes = distance((left_eye_center_x, left_eye_center_y),
                           (right_eye_center_x, right_eye_center_y))
    
    mouth_center_top_lip_x = pts_dict["mouth_center_top_lip_x"]
    mouth_center_top_lip_y = pts_dict["mouth_center_top_lip_y"]
    mouth_center_bottom_lip_x = pts_dict["mouth_center_bottom_lip_x"]
    mouth_center_bottom_lip_y = pts_dict["mouth_center_bottom_lip_y"]
    height_mouth = distance2((mouth_center_top_lip_x, mouth_center_top_lip_y),
                           (mouth_center_bottom_lip_x, mouth_center_bottom_lip_y))
    
    mouth_left_corner_x = pts_dict["mouth_left_corner_x"]
    mouth_left_corner_y = pts_dict["mouth_left_corner_y"]
    mouth_right_corner_x = pts_dict["mouth_right_corner_x"]
    mouth_right_corner_y = pts_dict["mouth_right_corner_y"]
    length_mouth = distance2((mouth_left_corner_x, mouth_left_corner_y),
                           (mouth_right_corner_x, mouth_right_corner_y))
    
    nose_tip_x = pts_dict["nose_tip_x"]
    nose_tip_y = pts_dict["nose_tip_y"]
    face_length = int(1.7 * distance2((mouth_left_corner_x, mouth_left_corner_y),
                           (mouth_right_corner_x, mouth_right_corner_y)))
    face_height = int(3 * distance2((nose_tip_x, nose_tip_y),
                           (mouth_center_top_lip_x, mouth_center_top_lip_y)))
    nose_tip=nose_tip_x+nose_tip_y
    eyebrow_distance=distance2((left_eyebrow_outer_end_x,left_eye_outer_corner_y),(right_eyebrow_outer_end_x,right_eyebrow_outer_end_y))    

    eyelength.append(mapper(round(length_eyes)))
    facelength.append(mapper(round(face_length)))
    faceheight.append(mapper(round(face_height)))
    eyebrowdistance.append(mapper(round(eyebrow_distance)))
    mouthheight.append(mapper(round(height_mouth)))
    mouthlength.append(mapper(round(length_mouth)))

    return 1
    

def variance():
    pt = str(mode(eyelength))+str(mode(faceheight))+str(mode(mouthheight))+str(mode(mouthlength))
    pt = hashlib.md5(pt.encode('utf-8')).hexdigest()
    file = open("diagnosticsdata.txt","a")
    file.write(pt)
    file.write("\n")
    file.close()
    return pt
   

def mapper(x):
    l=len(str(x))
    temp=x
    temp = temp%100
    temp2=int(x/100)
    if temp>=0 and temp<=25:
        temp=0
    if temp>25 and temp<=75:
        temp=50
    if temp>75:
        temp=100
    x=(temp2*100)+temp
    return x


def distance(pt1, pt2):
    pt1 = np.array(pt1)
    pt2 = np.array(pt2)
    return np.sqrt(sum((pt1-pt2)**2))

def distance2(pt1, pt2):
    p1,p2=pt1
    p3,p4=pt2
    p1=abs(p1-p2)
    p3=abs(p3-p4)
    p1=abs(p1-p3)
    return p1






    
    