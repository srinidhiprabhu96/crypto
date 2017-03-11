import numpy as np

def binary(n,s):
    """n - num
       s - no. of bits"""
    st = bin(n)
    out = np.zeros(s);
    for i in range(len(st)-1,1,-1):
        out[len(st)-1-i] = int(st[i])
    return out

def dec(a,s):
    """a - bit array of the form arr[x]
    s - no. of bits"""
    n = 0
    for i in range(0,len(a)):
        n+=a[i] * 2**i
    return n

def linearTable(sbox, size):
    """ inp params:
    sbox - truth table of sbox in a 2d array format : s[in,x]
    size - no. inp bits"""
    num = 2**size
    table = np.zeros((num, num))
    for a in range(0,num):
        ab = binary(a,size)
        for b in range(0,num):
            bb = binary(b,size)
            numzero = num
            for x in range(0,num):
                xor = 0
                xb = binary(x,size)
                for j in range(0,size):
                    xor ^= int(ab[j]*xb[j])
                    xor ^= int(bb[j]*sbox[x,j])
                if(xor == 1):
                    numzero -= 1
            table[a,b] = numzero
    return table

def diffTable(sbox, size):
    """ inp params:
    sbox - truth table of sbox in a 2d array format : s[in,x]
    size - no. inp bits"""
    num = 2**size
    table = np.zeros((num,num))
    for a in range(0,num):
        for x in range(0,num):
            y = dec(sbox[x],size)
            xs = x ^ a
            ys = dec(sbox[xs], size)
            b = y ^ ys
            table[a,b] += 1
    return table


def linearTableScore(table):
	""" Linear approximation table of an S-box. A lesser score implies a better S-Box"""
	num_elems = table.shape[0]*table.shape[1]
	half = table.shape[0]/2
	count = 0
	for i in range(1,table.shape[0]):
		for j in range(0,table.shape[1]):
			if i!=0 or j != 0:
				a = abs(table[i,j]-half)
				if a > count:
					count = a
	return float(count)/table.shape[1]

def diffTableScore(table):
	"""Differential distribution table of an S-box. A lesser score implies a better S-Box"""
	num_elems = table.shape[0]*table.shape[1]
	count = 0
	max_val = 0
	for i in range(1,table.shape[0]):
		count = table[i].max()
		if max_val < count:
			max_val = count
	return float(max_val)/table.shape[1]

def processLinTable(table):
    """Returns the table with entries as bias values. Input should be a numpy.array object"""
    tot = table.shape[0]
    table = table / float(tot)
    table = table - 0.5
    return table

def processDiffTable(table):
    """Returns the table with entries as bias values. Input should be a numpy.array object"""
    tot = table.shape[0]
    table = table / tot
    return table

# my_data = np.genfromtxt('linearTables/SBOX1_lineartable.csv', delimiter=',')
#
# proc_data = processTable(my_data)
#
# print my_data[0][0]
# print proc_data[0][0]
