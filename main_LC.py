import numpy as np
from tables import *
from LC import *
"""
files = os.listdir("Sboxes")

for name in files:
	print name
	matrix = np.genfromtxt("LinearTables/"+name.replace(".csv","")+'_lineartable.csv',delimiter=',').astype(int)
	matrix1 = processTable(matrix)
	
	np.savetxt("LAT_bias/"+name.replace(".csv","")+"_linearbias.csv", matrix1, delimiter=",")
"""
	



output = np.array([1,1,1,1,1,1,1,1])
name = 'SBOX1'
matrix = np.genfromtxt("LAT_bias/"+name+'_linearbias.csv',delimiter=',')
print matrix
print get_biases_for_output(matrix,output)

