diffusion_layer = []
inv_diffusion_layer = []
def populate_diffusion_layer():	# This function populates the diffusion layer(according to the design) and then populates the inverse diffusion
	global diffusion_layer
	global inv_diffusion_layer
	diffusion_layer = []
	for i in range(0,16):
		for j in range(0,8):
			a = byte_bit_to_index(i,j)
			#b = byte_bit_to_index((8*(i-1)+(j-1))%16+1,(8*(i-1)+(j-1))/16+1)
			b = byte_bit_to_index((8*(i)+(j))%16,(8*(i)+(j))/16)
			diffusion_layer.append(b)
	inv_diffusion_layer = []
	for i in range(0,128):
		inv_diffusion_layer.append(0)
	for i in range(0,128):
		inv_diffusion_layer[diffusion_layer[i]] = i
		
def byte_bit_to_index(byte,bit):	# Conversion from (i,j) byte(i)-bit(j) to the corresponding index 
	return 8*(byte)+bit
		
populate_diffusion_layer()
print diffusion_layer
print inv_diffusion_layer

"""
for i in range(0,128):
	print inv_diffusion_layer[diffusion_layer[i]]
"""	
res = []		# res will store the inverse diffusion generated using the inverse function we designed.
for a in range(0,16):
	for b in range(0,8):
		if a < 8:
			res.append(byte_bit_to_index(2*b,a))
		else:
			res.append(byte_bit_to_index(2*b+1,a-8))
print res

# If inverse diffusion populated earlier and one generated now are different, it'll print "CUP"
for i in range(0,128):
	if inv_diffusion_layer[i] != res[i]:
		print "CUP"

# For confirming again, we print res[diffusion_layer[i]] and we get i.
for i in range(0,128):
	print res[diffusion_layer[i]]	
