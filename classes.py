import random
import numpy as np


##############################################
# Functions used in the genetic algorithm    #
##############################################

req_matrix = None

def generate_individual(n):
	""" Generates a Boolean function with n-input bits """
	ind = []
	for i in range(0,pow(2,n)):
		a = random.randint(0,1)
		ind.append(a)
	#print len(ind)
	#print ind
	return np.array(ind)
	
def balanced_score(vector):
	""" Returns a score based on the balancedness of the boolean function. More balanced implies the score is close to 100 """
	n = vector.size
	ones = vector.sum()
	score = 100 - abs(float(((ones - n/2)*200))/n)
	return score

	
def fitness_function(vector,coeffs):
	""" Returns the fitness based on the coefficients and boolean functions """
	return coeffs[0]*balanced_score(vector) + coeffs[1]*non_linearity(vector) + coeffs[2]*SAC(vector)
	
def hamming_distance(vector1, vector2):
	""" Computes the hamming distance between vector1 and vector2 """
	return np.bitwise_xor(vector1,vector2).sum()
	
def non_linearity(vector):
	""" Returns the non-linearity score(out of 100) for a boolean function. A bent function will have a score of 100."""
	n = int(np.log2(vector.shape[0]))
	min_non_lin = vector.shape[0]
	max_non_lin = pow(2,n-1) - pow(2,n/2-1)	
	matrix = walsh_hadamand(n)	
	
	for i in range(0,matrix.shape[0]):
		hd = hamming_distance(vector,matrix[i])		
		hd = min(hd, vector.shape[0] - hd)
		if hd < min_non_lin:			
			min_non_lin = hd
	return float((min_non_lin*100))/max_non_lin
	
def SAC_balanced(vector,num):
	""" Returns the balancedness after XORing with a vector of HW(1). The vector of HW(1) is input as a decimal number in the variable 'num'."""
	result = np.zeros(vector.shape)	
	for i in range(0,vector.shape[0]):
		result[i] = vector[i] ^ vector[i^num]
	score = balanced_score(result)
	return score
	
def SAC(vector):
	""" Returns a SAC score out of 100 """
	n = int(np.log2(vector.shape[0]))
	count = 0
	for i in range(0,n):
		count += SAC_balanced(vector,pow(2,i))
	return float((count))/n
	
def populate_matrix(n):
	""" Stores the walsh hadamand matrix in a global variable for efficient lookup """
	global req_matrix
	req_matrix = []
	for i in range(0,n+1):
		req_matrix.append(walsh1(i))
	return req_matrix
	
def walsh_hadamand(n):
	""" Returns the walsh hadamand matrix of appropriate dimension. """
	return req_matrix[n]
	
def walsh1(n):
	""" Computes the walsh hadamand matrix."""
	if n == 0:
		return np.zeros((1,1)).astype(int)
	m1 = walsh_hadamand(n-1)
	m2 = matrix_complement(m1)
	top = np.concatenate((m1,m1),axis=1).astype(int)
	bottom = np.concatenate((m1,m2),axis=1).astype(int)
	walsh_hadamand_matrix = np.concatenate((top,bottom),axis=0).astype(int)
	return walsh_hadamand_matrix
			
	
def matrix_complement(matrix):
	""" Matrix complement to compute the walsh hadamand matrix """
	
	result = np.zeros(matrix.shape)
	for i in range(0,matrix.shape[0]):
		for j in range(0,matrix.shape[1]):
			if matrix[i,j] == 0:
				result[i,j] = 1
			else:
				result[i,j] = 0
	
	return result

"""	
Functions used when the condition that the output should be a permutation was enforced. This condition is not needed.


def convert_perm_to_ordinal(permutation):
	n = permutation.shape[0]
	ordinal = np.zeros(n)
	temp = np.ones(n)
	
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
	
def fitness_function_perm(output,coeffs):
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
	return coeffs[0]*balancedness + coeffs[1]*non_lin + coeffs[2]*SACness """
