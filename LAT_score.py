from tables import *
import numpy as np

#### Computes the LAT score for a given SBox, if the LAT is already present in the "LinearTables" folder ##########
try:
	name = raw_input("Enter an SBOX name(from Sboxes folder): ")
	matrix = np.genfromtxt("LinearTables/"+name+'_lineartable.csv',delimiter=',').astype(int)
	print "LAT Score: "+str(linearTableScore(matrix))
except:
	print "Linear table not found"
