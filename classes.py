import random
import numpy as np
def generate_individual(n):
	ind = []
	for i in range(0,pow(2,n)):
		a = random.randint(0,1)
		ind.append(a)
	#print len(ind)
	#print ind
	return np.array(ind)
	
def balanced_score(vector):
	n = vector.size
	ones = vector.sum()
	score = 100 - abs(((ones - n/2)*200)/n)
	return score
	
	
def fitness_function(vector):
	return float(SAC(vector)) #+ float(non_linearity(vector)) + float(balanced_score(vector))
	return float(non_linearity(vector))
	#return float(balanced_score(vector))
	
def hamming_distance(vector1, vector2):
	return np.bitwise_xor(vector1,vector2).sum()
	
def non_linearity(vector):
	#print type(vector)
	n = int(np.log2(vector.shape[0]))
	min_non_lin = vector.shape[0]
	max_non_lin = pow(2,n-1) - pow(2,n/2-1)
	matrix = walsh_hadamand(n)
	#print matrix[0]
	#print vector
	for i in range(0,matrix.shape[0]):
		hd = hamming_distance(vector,matrix[i])
		#print hd
		if hd < min_non_lin:
			min_non_lin = hd
	return (min_non_lin*100)/max_non_lin
	
def SAC_balanced(vector,num):
	result = np.zeros(vector.shape)
	#print "Num" + str(num)
	for i in range(0,vector.shape[0]):
		#print i
		#print i ^ num
		result[i] = vector[i] ^ vector[i^num]
	score = balanced_score(result)
	return score
	
def SAC(vector):
	n = int(np.log2(vector.shape[0]))
	count = 0
	for i in range(0,n):
		count += SAC_balanced(vector,pow(2,i))
	return float((count))/n
	
def walsh_hadamand(n):
	if n == 0:
		return np.zeros((1,1)).astype(int)
	m1 = walsh_hadamand(n-1)
	m2 = matrix_complement(m1)
	top = np.concatenate((m1,m1),axis=1).astype(int)
	bottom = np.concatenate((m1,m2),axis=1).astype(int)
	wh_result = np.concatenate((top,bottom),axis=0).astype(int)
	return wh_result
			
	
def matrix_complement(matrix):
	#print matrix
	result = np.zeros(matrix.shape)
	for i in range(0,matrix.shape[0]):
		for j in range(0,matrix.shape[1]):
			if matrix[i,j] == 0:
				result[i,j] = 1
			else:
				result[i,j] = 0
	#print matrix
	return result
