from classes import *
import numpy as np
import random

pop_size = 100
p_cross = 0.8
p_mut = 0.001
num_vars = 8
num_iter = 100
population = []
max_fitness = 0
for i in range(0,pop_size):
	population.append(generate_individual(num_vars))
max_fit = population[0]
for i in range(0,num_iter):
	fitness = []
	for j in range(0,pop_size):
		fitness.append(fitness_function(population[j]))


	fitness = np.array(fitness)
	avg_fitness = fitness.sum()/pop_size
	print "Average fitness: "+str(i)+" "+str(avg_fitness)
	#max_fit = population[np.argmax(fitness)]
	if fitness_function(max_fit) > max_fitness:
		max_fitness = fitness_function(max_fit)
		max_fit = population[np.argmax(fitness)]
		print "Max fitness increased to " + str(max_fitness)
	fitness = fitness/(fitness.sum())
	#print fitness
	for j in range(0,fitness.shape[0]):
		if j != fitness.shape[0]-1:
			fitness[j+1] += fitness[j]
	#print fitness

	
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

#print hamming_distance(population[0],np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
#print walsh_hadamand(0)
#print walsh_hadamand(1)
#print non_linearity(np.array([0,1,1,1]))
print population[0]
#print SAC(population[0])
population[0] = max_fit
print balanced_score(population[0])
print non_linearity(population[0])
print SAC(population[0])
#print non_linearity(np.array([0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]))
#SAC(np.array([1,0,1,0]))

