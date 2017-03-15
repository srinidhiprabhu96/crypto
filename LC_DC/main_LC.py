import numpy as np
from LAT_DDT.tables import *
from LC import *
"""
# Code to find the linear bias tables.
files = os.listdir("../Sboxes")

for name in files:
	print name
	matrix = np.genfromtxt("../LinearTables/"+name.replace(".csv","")+'_lineartable.csv',delimiter=',').astype(int)
	matrix1 = processTable(matrix)
	np.savetxt("../LAT_bias/"+name.replace(".csv","")+"_linearbias.csv", matrix1, delimiter=",")
"""

populate_diffusion_layer() # Computes the diffusion layer


## Compute the max linear bias of each SBox.
max_biases = [-1]
for i in range(1,9):
	max_biases.append(get_max_bias_of_sbox(i))
#print max_biases


min_bias = -128*np.log10(2)
trail = []
max_bias = -1000*np.log(2)
index = -1
rounds = 20
# Code to find the trail with the maximum bias.
for i in range(1,129):
	output = [i]
	bias_reached = 0
	trail_here = []
	for j in range(0,rounds):
		affect = get_affecting_input_bits(output)
		trail_here.append((output,affect[1]))
		for sbox in affect[1]:
			bias_reached = bias_reached + np.log10(2) + np.log10(max_biases[sbox])
		if j != 0:
			output = get_bits_before_diffusion(affect)
		else:
			if i > 64:
				output = affect[0]
			else:
				output = [i]

	#print bias_reached
	if bias_reached > max_bias:
		max_bias = bias_reached
		trail = trail_here
		index = i
print "The most deadly linear trail occurs when we try to guess key bit "+str(index)
for i in range(0,rounds):
	print "In round "+str(rounds-i)
	print "The bits affected are: "+str(trail[i][0])
	print "The sboxes affected are: "+str(trail[i][1])
print "The maximum bias is pow(2,"+str(int(max_bias/np.log10(2)))+")"

if max_bias < min_bias:
	print "The number of rounds are sufficient"
else:
	print "We need to increase the number of rounds"


"""
# Code to find the max number of rounds to reach a bias of less than 1/pow(2,128). Our cipher should have at least these many rounds.

max_rounds = 0
for i in range(1,129):
	output = [i]
	j = 0
	bias_reached = 0
	while bias_reached > min_bias:
		affect = get_affecting_input_bits(output)
		for sbox in affect[1]:
			bias_reached = bias_reached + np.log10(2) + np.log10(max_biases[sbox])
		if j != 0:
			output = get_bits_before_diffusion(affect)
		else:
			if i > 64:
				output = affect[0]
			else:
				output = [i]
		j += 1
	if j > max_rounds:
		max_rounds = j
	print "For bit "+str(i)+" we need "+str(j)+" rounds, giving a bias of "+str(bias_reached)
print "Maximum number of rounds needed is "+str(max_rounds)
"""
