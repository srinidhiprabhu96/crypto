def get_biases_for_output(matrix,output):
	sum = 0
	for i in range(0,output.shape[0]):
		sum = sum*2+output[i]
	return matrix[sum,:]
