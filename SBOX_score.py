from classes import *
import numpy as np
import os

###########################################################
# Generates scores for every S-Box in the "Sboxes" folder #
###########################################################


files = os.listdir("Sboxes")

for name in files:
	print "### "+name.replace(".csv","")
	matrix = np.genfromtxt("Sboxes/"+name,delimiter=',').astype(int)
	print matrix
	print matrix.shape
	n = matrix.shape[1]
	bent = pow(2,n-1)-pow(2,n/2-1)
	balance = 0
	non_lin = 0
	SAC_score = 0
	populate_matrix(matrix.shape[1])
	for i in range(0,n):
		balance += balanced_score(matrix[:,i])
		non_lin += non_linearity(matrix[:,i])
		SAC_score += SAC(matrix[:,i])
	balance = balance/n
	non_lin = non_lin/n
	SAC_score = SAC_score/n
	print "Average balancedness: "+str(balance)
	print "Average non linearity score: "+str(non_lin)+ " which means an avg non linearity of "+str(int(non_lin/100*bent))
	print "Average SAC score: "+str(SAC_score)
	print "$$$\n"
