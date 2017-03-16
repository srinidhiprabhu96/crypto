import numpy as np

def arr2dec(a):
    bin_str = ''
    for i in range(a.shape[0]-1,-1,-1):
        bin_str += str(a[i])
    return int(bin_str, 2)

for i in range(1,9):
    out = 'sbox'+str(i)+' = {'
    sbox = np.genfromtxt('../Sboxes/SBOX'+str(i)+'.csv',delimiter=',').astype(int)
    dec = arr2dec(sbox[0])
    out += str(dec)
    for x in range(1,sbox.shape[0]):
        dec = arr2dec(sbox[x])
        out += ','+str(dec)
    out += '};\n'
    print out
