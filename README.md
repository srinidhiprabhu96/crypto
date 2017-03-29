Run "python AI/genetic_algorithm.py" to see the results.  

It uses genetic algorithms to find a good SBox.  

Summary of files  

AI/
classes.py - Has the functions for implementing the genetic algorithm  
genetic_algorithm.py - Runs the genetic algorithm by taking the relative importance of the criteria as input.  

LAT_DDT/
tables.py - Functions to generate LAT and DDT along with computing the scores.  
DDT_generator.py - Generates DDT for all SBOXes present in "Sboxes" folder.  
LAT_generator.py - Generates LAT for all SBOXes present in "Sboxes" folder.  

Scores/
DDT_score.py - Computes the DDT score for an SBOX if the corresponding table is present in the "DifferentialTables" folder.  
LAT_score.py - Computes the LAT score for an SBOX if the corresponding table is present in the "LinearTables" folder.  
SBOX_score.py - Computes the scores for all criteria and outputs the average over all output bits of the SBOX.  

LC_DC/
LC.py - Supporting functions for finding the deadliest linear and differential trail  
main_LC.py - Code for computing the minimum number of rounds and the maximum bias for 20 rounds.  
main_DC.py - Code for computing the minimum number of rounds(DC) and the maximum prop ratio for 20 rounds.  
