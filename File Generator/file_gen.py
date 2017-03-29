import random

#print random.randrange(256)

for i in range(5,21):
	print i
	size = pow(2,i)
	filename = str(i)+".txt"
	fp = open(filename,"wb")
	for i in range(0,size):
		n = random.randrange(256)
		fp.write(chr(n))
	fp.close()
