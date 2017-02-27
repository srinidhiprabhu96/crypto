import numpy as np

def binary(n,s):
    """n - num
       s - no. of bits"""
    st = bin(n)
    out = np.zeros(s);
    for i in range(len(st)-1,1,-1):
        out[len(st)-1-i] = int(st[i])
    return out


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

sbox = np.array([[1,1,1,0],
[0,1,0,0],
[1,1,0,1],
[0,0,0,1],
[0,0,1,0],
[1,1,1,1],
[1,0,1,1],
[1,0,0,0],
[0,0,1,1],
[1,0,1,0],
[0,1,1,0],
[1,1,0,0],
[0,1,0,1],
[1,0,0,1],
[0,0,0,0],
[0,1,1,1]])

sbox = np.fliplr(sbox)

print linearTable(sbox,4)
