#from reedsolo import RSCodec
import numpy as np
import random


class keyGeneration:

    def func_Length(self,vector):
        #return the length of any vector
        return len(vector)


    def binary_quantization(self,feature_vector,leng,avg):
        #take average of the feature vector, if element > average, 1, if not 0
        sum = 0
        binary_vector = []


        for i in feature_vector:
            if i>avg[i]:
                binary_vector.append(1)
            else:
                binary_vector.append(0)

        return binary_vector


    def get_random_seed(self,binary_vector,leng):
        str1 = ''
        for i in range (0,leng):
            str1+=str(binary_vector[i])

        return int(str1,2)
    '''
    def get_random_seed(self,binary_vector,leng):
        #generate random seed by taking the sum of binary vectors
        sum = 0
        for i in range(0,leng):
            sum+=binary_vector[i]
        return sum
    '''


    def random_select(self,seed_, m):
        #random select two index
        np.random.seed(seed_)
        s1 = np.random.randint(m)
        s2 = np.random.randint(m)
        print(s1,s2)

        return s1,s2



    def random_permutation(self,binary_vector,leng,m):
        #random permutation using numpy shuffle, do random selection select two of them

        seed_ = self.get_random_seed(binary_vector,leng)
        shuffle_list = np.array(binary_vector)
        permutation_list = []

        for i in range(0,m):
            np.random.seed(seed_+i)
            np.random.shuffle(shuffle_list)
            print(shuffle_list)
            permutation_list.append(shuffle_list.tolist())

        s1,s2 = self.random_select(seed_,m)

        return permutation_list[s1],permutation_list[s2]

    '''
    def get_permutation_matrix(seed_):

        l = ['00','01','10','11']

        random.seed(seed_)
        random.shuffle(l)

        print(l)

        return l

    def random_permutation(self,binary_vector,leng,m):

        permutations_list = binary_vector

        seed_ = self.get_random_seed(binary_vector,leng)
        permutations = self.get_permutation_matrix(seed_)

        for i in range(0,leng,2):
            two_byte = str(binary_vector[i])+str(binary_vector)

            if two_byte == '00':
                permutations_list[i] = int(permutations[0][0])
                permutations_list[i+1] = int(permutations[0][1])
            if two_byte == '01':
                permutations_list[i] = int(permutations[1][0])
                permutations_list[i+1] = int(permutations[1][1])
            if two_byte == '10':
                permutations_list[i] = int(permutations[2][0])
                permutations_list[i+1] = int(permutations[2][1])
            if two_byte == '11':
                permutations_list[i] = int(permutations[3][0])
                permutations_list[i+1] = int(permutations[3][1])

        s1,s2 = self.random_select(seed_,m)

        return permutations_list[s1],permutations_list[s2]
    '''

    def list_xor(self,list1,list2,leng):
        #return the xor of two list
        result = []
        for i in range(0,leng):
            result.append(list1[i]^list2[i])

        return result


    def gen_keystring(self,list1,list2,leng):

        k_list = self.list_xor(list1,list2,leng)
        key = ''
        for i in range(0,leng):
            key+=str(k_list[i])

        return key


    '''
    def func_reedsolo_encode(feature_vector):
        rs = RSCodec(6)
        vector_encode = rs.encode(feature_vector)

        print(vector_encode)

    func_reedsolo_encode(feature_vector)


    def func_cosim(v1,v2):
        V1 = np.array(v1)
        V2 = np.array(v2)
        return 1.0/(1.0+np.linalg.norm(V1-V2))
    '''

    def jaccard_binary(self,x,y):
        #return tje jaccard difference between two binary lists.
        intersection = np.logical_and(x, y)
        union = np.logical_or(x, y)
        similarity = intersection.sum() / float(union.sum())

        return similarity




v1 = [1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0]
v2 = [1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0]

binary_vector = [1,0,1,0,0,0,1,0,1,1]
#np.random.seed(get_random_seed(binary_vector,func_Length(binary_vector)))
a = keyGeneration()
v3 = [1,2,3,4,5,1,4,16,1,3,2]
v4 = np.array(v3)
print(a.random_permutation(binary_vector,10,10))
