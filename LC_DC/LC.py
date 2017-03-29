import numpy as np
from LAT_DDT.tables import *

diffusion_layer = None
inv_diffusion_layer = None

def populate_diffusion_layer():
	global diffusion_layer
	global inv_diffusion_layer
	diffusion_layer = [-1]
	for i in range(1,17):
		for j in range(1,9):
			a = byte_bit_to_index(i,j)
			b = byte_bit_to_index((8*(i-1)+(j-1))%16+1,(8*(i-1)+(j-1))/16+1)
			diffusion_layer.append(b)
	inv_diffusion_layer = [-1]
	for i in range(1,129):
		inv_diffusion_layer.append(0)
	for i in range(1,129):
		inv_diffusion_layer[diffusion_layer[i]] = i

def get_biases_for_output(matrix,output):
	sum = 0
	for i in range(0,output.shape[0]):
		sum = sum*2+output[i]
	return matrix[sum,:]

def get_bits(sbox,odiff,w):
	binary = np.binary_repr(odiff,width=w)
	bit_list = []
	start = (sbox-1)*8
	for i in range(0,len(binary)):
		if binary[i] == '1':
			bit_list.append(start+1+i)
	return bit_list

#sbox is an integer
def get_max_bias_of_sbox(sbox):
	matrix = np.genfromtxt("../LinearTables/SBOX"+str(sbox)+'_lineartable.csv',delimiter=',')
	return linearTableScore(matrix)

def get_max_prop_of_sbox(sbox):
	matrix = np.genfromtxt("../DifferentialTables/SBOX"+str(sbox)+'_difftable.csv',delimiter=',')
	return diffTableScore(matrix)

#Assumption is that bit numbers are from 1 to 128
#Sbox numbers are from 1 to 8
def get_affecting_input_bits(output):
	bit_list = []	#The surely affected bits from the previous round.
	sbox_list = []	#The Sboxes that are affected in the previous round.
	for i in range(0,len(output)):
		if output[i] > 64:
			bit_list.append(output[i]-64)
		else:
			bit_list.append(output[i]+64)
			sbox_num = ((output[i]-1)/8)+1
			if sbox_num not in sbox_list:
				sbox_list.append(sbox_num)
	affect = (bit_list,sbox_list)
	return affect

#Byte numbers are from 1 to 16, bit numbers are from 1 to 8 for each sbox
def get_bits_before_diffusion(affect):
	bit_list = [] 	#The bits that need to be affected before diffusion to affect the given bits and sboxes.
	output = affect[0]
	for i in range(0,len(output)):
		bit_list.append(inv_diffusion_layer[output[i]])

	sboxes = affect[1]
	for sbox in sboxes:
		prev_bits = get_sbox_inverse_diff_bits(sbox)
		prev_boxes = []
		for prev in prev_bits:
			val = get_sbox_num(prev)
			if val != -1:
				prev_boxes.append((val,prev))
		prev_bit_boxes = []
		for bit in bit_list:
			val = get_sbox_num(bit)
			if val != -1:
				prev_bit_boxes.append((val,bit))
		flag = 0
		for i in range(0,len(prev_boxes)):
			for j in range(0,len(prev_bit_boxes)):
				if prev_boxes[i][0] == prev_bit_boxes[j][0] and prev_boxes[i][1] not in bit_list:
					bit_list.append(prev_boxes[i][1])
					flag = 1
					break
			if flag == 1:
				break
		if flag == 0:
			bit_list.append(prev_boxes[0][1])


	return list(set(bit_list))

def get_sbox_num(index):
	num = (index-1)/8 + 1
	if num > 8:
		return -1
	return num

def get_sbox_inverse_diff_bits(sbox):
	indices = []
	if sbox > 8:
		return indices
	indices = inv_diffusion_layer[(sbox-1)*8+1:(sbox)*8+1]
	return indices

def byte_bit_to_index(byte,bit):
	return 8*(byte-1)+bit
