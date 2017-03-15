from classes import *
import numpy as np
import random
import heapq
import sys
sys.path.insert(0,"../LAT_DDT")
from tables import *

####################################################################
# This code takes the relative importances of each criterion and   #
# uses simulated annealing to compute highly fit Boolean functions #
####################################################################

#coeffs = raw_input("Enter the coefficients for balancedness, non-linearity and SAC score(all values between 0 and 1 and sum should be 1): ")
#coeffs = map(float,coeffs.split())
coeffs = (0,0,1)
""" Parameters for simulated annealing. Change these parameters in the file, if needed."""
num_vars = 8
outputs = 8
num_iter = 100
max_fitness = 0
n = pow(2,num_vars)
SBOX = []
global_max = []
global_SBOX = []
T = pow(10,2)
eps = 0.001

populate_matrix(outputs) #generates and stores the walsh-hadamand matrix, for faster computation




#print node
#print generate_neighbour(node)

for i in range(0,8):
	print i
	T = pow(10,2)
	node = generate_individual(num_vars)
	best_node = node
	best_val = fitness_function(node,coeffs)
	count = 0
	while T > 1:
		count += 1
		#print (T,count)
		for i in range(0,1):
			neighbour = generate_neighbour(node)
			next_val = fitness_function(neighbour,coeffs)
			curr_val = fitness_function(node,coeffs)
			if next_val > best_val:
				best_val = next_val
				best_node = neighbour
				print "Best: "+str(best_val)
			E_diff =  next_val - curr_val
			prob = random.uniform(0,1)
			#print prob
			#print float(1)/(1+np.exp(-E_diff/float(T)))
			if prob < float(1)/(1+np.exp(-E_diff/float(T))):
				node = neighbour
		T -= eps*T
	print best_val
	print "Balancedness of output functions: "+ str(balanced_score(best_node))
	print "Non-linearity of output functions: "+str(non_linearity(best_node))
	print "SAC score of output functions: "+str(SAC(best_node))
	SBOX.append(best_node)

SBOX = np.array(SBOX)
SBOX = SBOX.transpose()
### Save S-Box as csv file, if needed. The file will be saved in the 'Sboxes' folder ##########
c = raw_input("\n\nDo you want to save this sbox?(y/n): ")
if c == 'y':
	name = raw_input("Enter the sbox name: ")
	np.savetxt("../Sboxes/"+name+".csv", SBOX, delimiter=",")
	print "SAVED"
############## END ############################################################################
"""
while T > 1:
	count += 1
	print (T,count)
	for i in range(0,1):
		neighbour = generate_neighbour(node)
		next_val = fitness_function(neighbour,coeffs)
		curr_val = fitness_function(node,coeffs)
		if next_val > best_val:
			best_val = next_val
			best_node = neighbour
			print "Best: "+str(best_val)
		E_diff =  next_val - curr_val
		prob = random.uniform(0,1)
		print prob
		print float(1)/(1+np.exp(-E_diff/float(T)))
		if prob < float(1)/(1+np.exp(-E_diff/float(T))):
			node = neighbour
	T -= eps*T
print best_val
print "Balancedness of output functions: "+ str(balanced_score(best_node))
print "Non-linearity of output functions: "+str(non_linearity(best_node))
print "SAC score of output functions: "+str(SAC(best_node))
"""
