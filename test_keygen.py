from keyGeneration import keyGeneration

feature_vector = []
keygen = keyGeneration()


leng = keygen.func_Length(feature_vector)
m = leng

binary_vector = keygen.binary_quantization(feature_vector,leng)
permutation = keygen.random_permutation(binary_vector,leng,m)
keystring = keygen.gen_keystring(permutation[0],permutation[1],leng)