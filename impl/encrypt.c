// This program takes 2 command line arguments as input - the plaintext file(to be encrypted) and the file to write the cipher text. 
#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include "common.c"

// Function to encrypt an entire file using counter mode.
void encrypt_file(char *pt_file, char *ct_file, __uint128_t key)
{
	FILE *fpr, *fpw;
	__uint128_t counter = 0xabcdef0987654321, block;
	union bits128 pt,ct;
	fpr = fopen(pt_file,"r");
	fpw = fopen(ct_file,"w");
	int size,i,n;
	fseek(fpr, 0L, SEEK_END);
	size = ftell(fpr);
	rewind(fpr);
	if(size % 16 != 0)
	{
		printf("The file size should be a multiple of 16 bytes\n");
		exit(0);
	} 
	n = size/16;
	clock_t time = 0,start,end;
	for(i=0;i<n;i++)
	{
		pt = read_16_bytes(fpr);
		block = encrypt(pt.integer, key);
		
		//ct.integer = pt.integer ^ block;
		ct.integer = block;
		write_16_bytes(fpw, ct);
		counter++;
	}
}



int main(int argc, char *argv[])
{
	if(argc != 4)
	{
		printf("Usage: ./encrypt <PT_file> <CT_file> <Key file>\n");
		exit(0);
	}
	union bits128 key;
	FILE *fp;
	fp = fopen(argv[3],"r");
	key = read_16_bytes(fp);
	encrypt_file(argv[1],argv[2],key.integer);
	return 0;
}
