from classes import *
import numpy as np
import random

coeffs = raw_input("Enter the coefficients for balancedness, non-linearity and SAC score(all values between 0 and 1 and sum should be 1): ")
coeffs = map(float,coeffs.split())
print coeffs
population_size = 100
p_cross = 0.8
p_mut = 0.001
num_vars = 4
num_iter = 100
population = []
ordinal_pop = []
max_fitness = 0
n = pow(2,num_vars)
for i in range(0,population_size):
	population.append(np.random.permutation(n))
for i in range(0,population_size):
	ordinal_pop.append(convert_perm_to_ordinal(population[i]))
#for i in range(0,pop_size):
#	print ordinal_pop[i]
global_max = 0
for i in range(0,num_iter):
	print "Iter: "+str(i)
	fitness_array = []
	for j in range(0,population_size):
		perm = convert_ordinal_to_perm(ordinal_pop[j])
		#print perm
		fitness_array.append(fitness_function(ordinal_pop[j],coeffs))
	#print fitness_array	
	
	fitness_array = np.array(fitness_array)
	#print "Average fitness: "+str(fitness_array.sum()/population_size)
	fitness_array = fitness_array/(fitness_array.sum())
	#print fitness_array
	max_fit = ordinal_pop[np.argmax(fitness_array)]
	#print max_fit
	#perm = convert_ordinal_to_perm(max_fit)
	max_fit_val = fitness_function(max_fit,coeffs)
	if max_fit_val > global_max:
		print "Found a better soln in iter "+str(i)
		global_max = max_fit_val
		print global_max
		#print perm
	for j in range(0,fitness_array.shape[0]):
		if j != fitness_array.shape[0]-1:
			fitness_array[j+1] += fitness_array[j]
	#print fitness_array
	
	selected = []
	for j in range(0,population_size):
		curr = random.uniform(0,1)
		for k in range(0,len(fitness_array)):
			if fitness_array[k] > curr:
				break
		selected.append(ordinal_pop[k])
	
	crossed = []
	
	for j in range(0,population_size,2):
		curr = random.uniform(0,1)
		for k in range(0,len(fitness_array)):
			if fitness_array[k] > curr:
				break
		p1 = ordinal_pop[k]
		curr = random.uniform(0,1)
		for k in range(0,len(fitness_array)):
			if fitness_array[k] > curr:
				break
		p2 = ordinal_pop[k]
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
	
	ordinal_pop = crossed

print max_fit
a = get_Sbox_output(max_fit)
print a
for i in range(0,a.shape[1]):
	print "Bit "+str(i)
	print "Balancedness: "+ str(balanced_score(a[:,i]))
	print "Non-linearity: "+ str(non_linearity(a[:,i]))
	print "SACness: " + str(SAC(a[:,i]))
