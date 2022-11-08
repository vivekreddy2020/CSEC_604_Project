import cv2
import numpy as np
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

def apply_filter(frame, pts_dict):

    left_eye_center_x = pts_dict["left_eye_center_x"]
    left_eye_center_y = pts_dict["left_eye_center_y"]
    left_eye_inner_corner_x = pts_dict["left_eye_inner_corner_x"]
    left_eye_inner_corner_y = pts_dict["left_eye_inner_corner_y"]
    left_eye_outer_corner_x = pts_dict["left_eye_outer_corner_x"]
    left_eye_outer_corner_y = pts_dict["left_eye_outer_corner_y"]
    left_eyebrow_outer_end_x = pts_dict["left_eyebrow_outer_end_x"]
    left_eyebrow_outer_end_y = pts_dict["left_eyebrow_outer_end_y"]
    radius_left = distance((left_eye_center_x, left_eye_center_y),
                           (left_eye_inner_corner_x, left_eye_inner_corner_y))

    right_eye_center_x = pts_dict["right_eye_center_x"]
    right_eye_center_y = pts_dict["right_eye_center_y"]
    right_eye_outer_corner_x = pts_dict["right_eye_outer_corner_x"]
    right_eye_outer_corner_y = pts_dict["right_eye_outer_corner_y"]
    right_eye_inner_corner_x = pts_dict["right_eye_inner_corner_x"]
    right_eye_inner_corner_y = pts_dict["right_eye_inner_corner_y"]
    right_eyebrow_outer_end_x = pts_dict["right_eyebrow_outer_end_x"]
    right_eyebrow_outer_end_y = pts_dict["right_eyebrow_outer_end_y"]
    radius_right = distance((right_eye_center_x, right_eye_center_y),
                           (right_eye_inner_corner_x, right_eye_inner_corner_y))
    
    radius_eyes = distance((right_eye_center_x, right_eye_center_y),
                           (right_eyebrow_outer_end_x, right_eyebrow_outer_end_y))
    
    length_eyes = distance((left_eye_center_x, left_eye_center_y),
                           (right_eye_center_x, right_eye_center_y))
    
    mouth_center_top_lip_x = pts_dict["mouth_center_top_lip_x"]
    mouth_center_top_lip_y = pts_dict["mouth_center_top_lip_y"]
    mouth_center_bottom_lip_x = pts_dict["mouth_center_bottom_lip_x"]
    mouth_center_bottom_lip_y = pts_dict["mouth_center_bottom_lip_y"]
    height_mouth = distance((mouth_center_top_lip_x, mouth_center_top_lip_y),
                           (mouth_center_bottom_lip_x, mouth_center_bottom_lip_y))
    
    mouth_left_corner_x = pts_dict["mouth_left_corner_x"]
    mouth_left_corner_y = pts_dict["mouth_left_corner_y"]
    mouth_right_corner_x = pts_dict["mouth_right_corner_x"]
    mouth_right_corner_y = pts_dict["mouth_right_corner_y"]
    length_mouth = distance((mouth_left_corner_x, mouth_left_corner_y),
                           (mouth_right_corner_x, mouth_right_corner_y))
    
    nose_tip_x = pts_dict["nose_tip_x"]
    nose_tip_y = pts_dict["nose_tip_y"]
    face_length = int(1.7 * distance((mouth_left_corner_x, mouth_left_corner_y),
                           (mouth_right_corner_x, mouth_right_corner_y)))
    face_height = int(3 * distance((nose_tip_x, nose_tip_y),
                           (mouth_center_top_lip_x, mouth_center_top_lip_y)))
    nose_tip=nose_tip_x+nose_tip_y
    eyebrow_distance=distance((left_eyebrow_outer_end_x,left_eye_outer_corner_y),(right_eyebrow_outer_end_x,right_eyebrow_outer_end_y))
    
    frame = left_eye_center_x+right_eye_center_x+left_eye_inner_corner_x+left_eye_inner_corner_y+left_eye_outer_corner_x+left_eye_outer_corner_y+left_eyebrow_outer_end_x+left_eyebrow_outer_end_y+right_eye_center_y+right_eye_inner_corner_x+right_eye_inner_corner_y+right_eye_outer_corner_x+right_eye_outer_corner_y+right_eyebrow_outer_end_x+right_eyebrow_outer_end_y+radius_left+radius_right+radius_eyes+length_eyes+length_mouth
    

    print("eyes_length:"+str(round(length_eyes)))
    
    print("facelength:"+str(round(face_length)))
    
    print("faceheight:"+str(round(face_height)))
    
    print("eyebrowdistance:"+str(round(eyebrow_distance)))
    
    print("mouthheight:"+str(round(height_mouth)))
    
    print("mouthlength:"+str(round(length_mouth)))
    
    eyelength.append(round(length_eyes))
    facelength.append(round(face_length))
    faceheight.append(round(face_height))
    eyebrowdistance.append(round(eyebrow_distance))
    mouthheight.append(round(height_mouth))
    mouthlength.append(round(length_mouth))

    return int(frame/1000)


def variance():
    avg=int(sum(eyelength)/len(eyelength))
    for i in range(len(eyelength)):
        eyelength_var.append(abs(avg-eyelength[i]))
    print(max(eyelength_var))
    avg=int(sum(facelength)/len(facelength))
    for i in range(len(facelength)):
        facelength_var.append(abs(avg-facelength[i]))
    print(max(facelength_var))
    avg=int(sum(faceheight)/len(faceheight))
    for i in range(len(faceheight)):
        faceheight_var.append(abs(avg-faceheight[i]))
    print(max(faceheight_var))
    avg=int(sum(eyebrowdistance)/len(eyebrowdistance))
    for i in range(len(eyebrowdistance)):
        eyebrowdistance_var.append(abs(avg-eyebrowdistance[i]))
    print(max(eyebrowdistance_var))
    avg=int(sum(mouthlength)/len(mouthlength))
    for i in range(len(mouthlength)):
        mouthlength_var.append(abs(avg-mouthlength[i]))
    print(max(mouthlength_var))
    avg=int(sum(mouthheight)/len(mouthheight))
    for i in range(len(mouthheight)):
        mouthheight_var.append(abs(avg-mouthheight[i]))
    print(max(mouthheight_var))




def distance(pt1, pt2):
    pt1 = np.array(pt1)
    pt2 = np.array(pt2)
    return np.sqrt(sum((pt1-pt2)**2))

if __name__ == '__main__':
    model = FaceKeypointsCaptureModel("face_model.json", "face_model.h5")




    
    