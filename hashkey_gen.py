import math
import numpy as np

def cal_dist(p1,p2):
    #calculate the distance between two sample points
    dist = 0.0
    dist = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    return dist

def cal_part(sample_list, init_p, p):

    part_sample_list = []

    for i in range (init_p,init_p+5):
        part_sample_list.append(cal_dist(sample_list[i-1],p))

    return np.array(part_sample_list)

def feature_cal(sample_list):

    dist_0 = cal_dist(sample_list[27],sample_list[57]) #the eyebro center to the lower lip is the base

    dist_le = cal_part(sample_list,37,sample_list[28]) #the list contains distance from point 37-41 to 29
    dist_lb = cal_part(sample_list,18,sample_list[27]) #the list contains distance from point 18-22 to 28
    dist_nh = cal_part(sample_list,28,sample_list[31]) #the list contains distance from point 28-34 to 32
    dist_nw = cal_part(sample_list,32,sample_list[51]) #the list contains distance from point 32-36 to 52
    dist_mw = cal_part(sample_list,56,sample_list[51]) #the list contains distance from point 56-60 to 52
    dist_lf = cal_part(sample_list,4,sample_list[48]) #the list contains distance from point 4-8 to 49

    feature_list = np.append(dist_le,dist_lb)
    feature_list = np.append(feature_list,dist_nh)
    feature_list = np.append(feature_list,dist_nw)
    feature_list = np.append(feature_list,dist_mw)
    feature_list = np.append(feature_list,dist_lf)

    return feature_list/dist_0
