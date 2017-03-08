Run "python geentic_algorithm.py" to see the results.  

It uses genetic algorithms to find a good SBox.  

Summary of files  

classes.py - Has the functions for implementing the genetic algorithm  
DDT_generator.py - Generates DDT for all SBOXes present in "Sboxes" folder.  

DDT_score.py - Computes the DDT score for an SBOX if the corresponding table is present in the "DifferentialTables" folder.  

genetic_algorithm.py - Runs the genetic algorithm by taking the relative importance of the criteria as input.  

LAT_generator.py - Generates LAT for all SBOXes present in "Sboxes" folder.  

LAT_score.py - Computes the LAT score for an SBOX if the corresponding table is present in the "LinearTables" folder.  

SBOX_score.py - Computes the scores for all criteria and outputs the average over all output bits of the SBOX.  

tables.py - Functions to generate LAT and DDT along with computing the scores.  
