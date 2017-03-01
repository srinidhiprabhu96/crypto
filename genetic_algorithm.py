from classes import *
from tables import *
import numpy as np
import random
import heapq

####################################################################
# This code takes the relative importances of each criterion and   #
# uses a genetic algorithm to compute highly fit Boolean functions #
####################################################################

coeffs = raw_input("Enter the coefficients for balancedness, non-linearity and SAC score(all values between 0 and 1 and sum should be 1): ")
coeffs = map(float,coeffs.split())

""" Parameters for the genetic algorithm. Change these parameters in the file, if needed."""
pop_size = 100
p_cross = 0.8
p_mut = 0.001
num_vars = 8
outputs = 8
num_iter = 100
population = []
ordinal_pop = []
max_fitness = 0
n = pow(2,num_vars)
SBOX = []
global_max = []
global_SBOX = []

populate_matrix(outputs) #generates and stores the walsh-hadamand matrix, for faster computation

### Generate initial population ###
for i in range(0,pop_size):
	population.append(generate_individual(num_vars))
###################################	
	
max_fit = population[0]

#### Iterate for a fixed number of iterations ###
for i in range(0,num_iter):
	fitness = []
	for j in range(0,pop_size):
		fitness.append(fitness_function(population[j],coeffs))
	
	########## Take the n most-fit individuals obtained till now. n is the number of outputs. ##########
	global_SBOX = global_SBOX + population
	global_max = global_max + fitness
	results = heapq.nlargest(outputs,global_max)
	tempbox = []
	for z in range(0,len(results)):
		indx = global_max.index(results[z])
		tempbox.append(global_SBOX[indx])
		del global_max[indx]
		del global_SBOX[indx]
	global_SBOX = tempbox
	global_max = results	
	###################
	
	fitness = np.array(fitness)
	avg_fitness = fitness.sum()/pop_size
	
	max_fit = population[np.argmax(fitness)]
	if fitness_function(max_fit,coeffs) > max_fitness:
		max_fitness = fitness_function(max_fit,coeffs)
		max_fit = population[np.argmax(fitness)]
		
	fitness = fitness/(fitness.sum())
	
	for j in range(0,fitness.shape[0]):
		if j != fitness.shape[0]-1:
			fitness[j+1] += fitness[j]
	
	############## Crossover operation in the genetic algorithm ##########
	crossed = []
	for j in range(0,pop_size,2):
		curr = random.uniform(0,1)
		for k in range(0,len(fitness)):
			if fitness[k] > curr:
				break
		p1 = population[k]
		curr = random.uniform(0,1)
		for k in range(0,len(fitness)):
			if fitness[k] > curr:
				break
		p2 = population[k]
	
		index = np.random.randint(0,p1.shape[0])

		p = random.uniform(0,1)
		if p < p_cross:
			c1 = np.append(p1[:index],p2[index:]) 
			c2 = np.append(p2[:index],p1[index:]) 
		else:
			c1 = p1
			c2 = p2
	
	
		crossed.append(c1)
		crossed.append(c2)
	##########################################################
	
	#### Mutation operation in the genetic algorithm #########
	for j in range(0,len(crossed)):
		curr = random.uniform(0,1)
		if curr < p_mut:
			#print "Mutated"
			p1 = crossed[j]
			#print crossed[j]
			index = np.random.randint(0,p1.shape[0])
			if p1[index] == 0:
				p1[index] = 1
			else:
				p1[index] = 0
			crossed[j] = p1
			#print crossed[j]
			#print "End of mutation"
	population = crossed
	########################################################
	
#################################################	


######### Compute and print the Sbox scores ##########
global_SBOX = np.array(global_SBOX)
global_SBOX = global_SBOX.transpose()
non_lin_arr = []
b_array = []
sac_array = []
for z in range(0,global_SBOX.shape[1]):
	non_lin_arr.append(non_linearity(global_SBOX[:,z]))
	b_array.append(balanced_score(global_SBOX[:,z]))
	sac_array.append(SAC(global_SBOX[:,z]))
print "Overall fitness of output functions: "+str(global_max)
print "Balancedness of output functions: "+ str(b_array)
print "Non-linearity of output functions: "+str(non_lin_arr)
print "SAC score of output functions: "+str(sac_array)
print "Final S-Box"
print global_SBOX
#####################################################


### Save S-Box as csv file, if needed. The file will be saved in the 'Sboxes' folder ##########
c = raw_input("\n\nDo you want to save this sbox?(y/n): ")
if c == 'y':
	name = raw_input("Enter the sbox name: ")
	np.savetxt("Sboxes/"+name+".csv", global_SBOX, delimiter=",")
	print "SAVED"
############## END ############################################################################
