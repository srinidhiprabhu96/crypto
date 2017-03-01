from classes import *
from tables import *
import numpy as np
import random
import os

###############################################
# Generates Differential Distribution Tables  #
# for every S-Box in the "Sboxes" folder      #
###############################################

#Loop over all sboxes in "Sboxes" folder to generate DDT
# Assuming all files are .csv files
files = os.listdir("Sboxes")
#print files

for name in files:
	print "###"+name
	matrix = np.genfromtxt("Sboxes/"+name,delimiter=',').astype(int)
	print matrix
	print matrix.shape
	table = diffTable(matrix,matrix.shape[1])
	print "Computed DDT"
	np.savetxt("DifferentialTables/"+name.replace(".csv","")+"_difftable.csv", table, fmt='%i', delimiter=",") 
	print "DDT saved"
	print "DDT score: "+str(diffTableScore(table))
	print "$$$"
	
"""
Single DDT generator
name = raw_input("Enter a filename(without extension): ")
matrix = np.genfromtxt("Sboxes/"+name+'.csv',delimiter=',').astype(int)
print matrix
print matrix.shape
table = diffTable(matrix,matrix.shape[1])
print "Computed DDT"
np.savetxt("DifferentialTables/"+name+"_difftable.csv", table, fmt='%i', delimiter=",") 
print "Table saved"
print "DDT score: "+str(diffTableScore(table)) 

"""
