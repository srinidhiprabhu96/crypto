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
	
def convert_perm_to_ordinal(permutation):
	n = permutation.shape[0]
	#print n
	ordinal = np.zeros(n)
	temp = np.ones(n)
	#print temp[:3].sum()
	for i in range(0,n):
		#print permutation[i]
		#print temp[:permutation[i]]
		ordinal[i] = int(temp[:permutation[i]].sum())
		#print permutation[i]
		temp[permutation[i]] = 0
	#print ordinal
	return ordinal.astype(int)
	
def get_Sbox_output(ordinal):
	perm = convert_ordinal_to_perm(ordinal)
	n = int(np.log2(ordinal.shape[0]))
	result = []
	for i in range(0,perm.shape[0]):
		#print perm[i]
		#print np.array(list(np.binary_repr(perm[i],width=n))).astype(int)
		result.append(np.array(list(np.binary_repr(perm[i],width=n))).astype(int))
	result = np.array(result)
	return result.astype(int)
	

	

def convert_ordinal_to_perm(ordinal):
	n = ordinal.shape[0]
	list1 = []
	for i in range(0,n):
		list1.append(i)
	permutation = []
	for i in range(0,n):
		#print list1
		#print ordinal[i] 
		permutation.append(list1[int(ordinal[i])])
		del list1[int(ordinal[i])]
	#print permutation
	return np.array(permutation).astype(int)
	
def fitness_function(output,coeffs):
	matrix = get_Sbox_output(output)
	n = matrix.shape[1]
	balancedness = 0
	non_lin = 0
	SACness = 0
	for i in range(0,n):
		#print matrix[:,i]
		balancedness += balanced_score(matrix[:,i])
		non_lin += non_linearity(matrix[:,i])
		SACness += SAC(matrix[:,i])
	balancedness = float(balancedness)/n
	non_lin = float(non_lin)/n
	SACness = float(SACness)/n
	return coeffs[0]*balancedness + coeffs[1]*non_lin + coeffs[2]*SACness
	
def hamming_distance(vector1, vector2):
	return np.bitwise_xor(vector1,vector2).sum()
	
def non_linearity(vector):
	#print type(vector)
	#print "###"
	n = int(np.log2(vector.shape[0]))
	min_non_lin = vector.shape[0]
	max_non_lin = pow(2,n-1) - pow(2,n/2-1)
	matrix = walsh_hadamand(n)
	#print matrix[0]
	#print vector
	for i in range(0,matrix.shape[0]):
		hd = hamming_distance(vector,matrix[i])
		#print hd
		#hd = min(hd, vector.shape[0] - hd)
		if hd < min_non_lin:			
			min_non_lin = hd
			#print min_non_lin
	#print "###___"
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
