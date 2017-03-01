from classes import *
from tables import *
import numpy as np
import random

##########################################
# Generates Linear Approximation Tables  #
# for every S-Box in the "Sboxes" folder #
##########################################


#Loop over all sboxes to generate LAT
# Assuming all files are .csv files
files = os.listdir("Sboxes")
#print files


for name in files:
	print "### "+name
	matrix = np.genfromtxt("Sboxes/"+name,delimiter=',').astype(int)
	print matrix
	print matrix.shape
	table = linearTable(matrix,matrix.shape[1])
	print "Computed LAT"
	np.savetxt("LinearTables/"+name.replace(".csv","")+"_lineartable.csv", table, fmt='%i', delimiter=",")
	print "LAT saved"
	print "LAT score: "+str(linearTableScore1(table))
	print "$$$"
	

"""
Single LAT generator
name = raw_input("Enter a filename(without extension): ")
matrix = np.genfromtxt("Sboxes/"+name+'.csv',delimiter=',').astype(int)
print matrix
print matrix.shape
table = linearTable(matrix,matrix.shape[1])
print "Computed LAT"
np.savetxt("LinearTables/"+name+"_lineartable.csv", table, fmt='%i', delimiter=",")
print "Table saved"
print "LAT score: "+str(linearTableScore(table))

"""
