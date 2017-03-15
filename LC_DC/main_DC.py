import numpy as np
from LAT_DDT.tables import *
from LC import *

populate_diffusion_layer()


## Compute the max linear bias of each SBox.
max_biases = [-1]
for i in range(1,9):
	max_biases.append(get_max_prop_of_sbox(i))
#print max_biases

min_bias = -128*np.log10(2)
max_rounds = 0


trail = []
max_bias = -1000*np.log(2)
index = -1
rounds = 20

# Code to find the trail with the maximum propagation ratio.
for i in range(1,17):
	for j in range(1,256):
		output = get_bits(i,j,8)
		bias_reached = 0
		trail_here = []
		for k in range(0,rounds):
			affect = get_affecting_input_bits(output)
			trail_here.append((output,affect[1]))
			for sbox in affect[1]:
				bias_reached = bias_reached + np.log10(2) + np.log10(max_biases[sbox])
			if k != 0:
				output = get_bits_before_diffusion(affect)
			else:
				if i > 8:
					output = affect[0]
				else:
					output = [i]

		#print bias_reached
		if bias_reached > max_bias:
			max_bias = bias_reached
			trail = trail_here
			index = (i,j)
print "The most deadly differential trail is"+str(index)
for i in range(0,rounds):
	print "In round "+str(rounds-i)
	print "The bits affected are: "+str(trail[i][0])
	print "The sboxes affected are: "+str(trail[i][1])
print "The maximum propagation ratio is pow(2,"+str(int(max_bias/np.log10(2)))+")"

if max_bias < min_bias:
	print "The number of rounds are sufficient"
else:
	print "We need to increase the number of rounds"


"""
# Code to find the minimum number of rounds
for i in range(1,9): #For each sbox
	for j in range(1,256): #For each output diff
		output = get_bits(i,j,8)
		k = 0
		bias_reached = 0
		while bias_reached > min_bias:
			affect = get_affecting_input_bits(output)
			for sbox in affect[1]:
				bias_reached = bias_reached + np.log10(max_biases[sbox])
			output = get_bits_before_diffusion(affect)
			k += 1
		if k > max_rounds:
			max_rounds = k
		print "For sbox "+str(i)+" and output diff "+str(j)+" we need "+str(k)+" rounds, giving a bias of "+str(bias_reached)
print "Maximum number of rounds needed is "+str(max_rounds)
"""
