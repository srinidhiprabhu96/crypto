import random

#print random.randrange(256)


#One file generator
i = 5
size = pow(2,i)
filename = "plaintext/"+str(i)+".txt"
fp = open(filename,"wb")
for i in range(0,size):
	n = random.randrange(256)
	#n = random.randrange(97,124)
	print n
	fp.write(chr(n))
fp.close()

"""
for i in range(5,21):
	size = pow(2,i)
	filename = str(i)+".txt"
	fp = open(filename,"wb")
	for i in range(0,size):
		n = random.randrange(256)
		fp.write(chr(n))
	fp.close()
"""
