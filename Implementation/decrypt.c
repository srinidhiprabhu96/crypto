// This program takes 2 command line arguments as input - the plaintext file(to be encrypted) and the file to write the cipher text. 
#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include "common.c"

// Function to encrypt an entire file using counter mode.
void decrypt_file(char *ct_file, char *dt_file, __uint128_t key)
{
	FILE *fpr, *fpw;
	__uint128_t counter = 0xabcdef0987654321, block;
	union bits128 dt,ct,block1,counter1;
	fpr = fopen(ct_file,"r");
	fpw = fopen(dt_file,"w");
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
		ct = read_16_bytes(fpr);
		block = encrypt(counter, key);
		dt.integer = ct.integer ^ block;
		//ct.integer = block;
		write_16_bytes(fpw, dt);
		counter++;
	}
}



int main(int argc, char *argv[])
{
	if(argc != 4)
	{
		printf("Usage: ./decrypt.out <PT_file> <CT_file> <Key file>\n");
		exit(0);
	}
	union bits128 key;
	FILE *fp;
	fp = fopen(argv[3],"r");
	key = read_16_bytes(fp);
	decrypt_file(argv[1],argv[2],key.integer);
	return 0;
}
