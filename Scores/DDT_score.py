import numpy as np
import sys
sys.path.insert(0,"../LAT_DDT")
from tables import *

#### Computes the DDT score for a given SBox, if the DDT is already present in the "DifferentialTables" folder ##########
try:
	name = raw_input("Enter an SBOX name(from Sboxes folder): ")
	matrix = np.genfromtxt("../DifferentialTables/"+name+'_difftable.csv',delimiter=',').astype(int)
	print "DDT Score: "+str(diffTableScore(matrix))
except:
	print "Differential table not found"
