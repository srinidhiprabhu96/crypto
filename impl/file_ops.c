#include<stdio.h>
#include<stdint.h>
#include "common.c"

// The space of this union is also 128 bits.
union bits128
{
    __uint128_t integer;
    unsigned char byte[16];
};

union bits128 read_16_bytes(FILE *fp)
{
	__uint128_t ret_val = 0;
	char buffer;
	int i;
	union bits128 block;
	//print.integer = ret_val;
	for(i=15;i>=0;i--)
	{
		fread(&buffer, 1, 1, fp);
		block.byte[i] = buffer;

	}
	return block;
}

void write_16_bytes(FILE *fpw, union bits128 print)
{
	int i;
	// This step depends on the endianness of the system.
	for(i=15;i>=0;i--)
	{
		fprintf(fpw,"%c",(int)print.byte[i]);
	}
}
// This code works fine, but the read and write functions return/expect a union.
/* union bits128 value,print;
	__uint128_t abc,def;
	value = read_16_bytes(fp);
	abc = value.integer; // Variable abc now has the 128 bit integer.
	def = function(abc);
	print.integer = def;
	write_16_bytes(print);
	For example, in the below code I just add 1 to the 128 bit integer and then write to file. I'm able to see that the values printed in the 2 files differ in the LSB of every 16 bit chunk.(Expected result/

*/
// For testing
int main()
{
	FILE *fp,*fpw,*fpw2;
	fp = fopen("plaintext.txt","rb");
	fpw = fopen("ciphertext.txt","wb");
	fpw2 = fopen("decrypted.txt","wb");
	char buffer;
	union bits128 value, cptxt, dectxt;
	value = read_16_bytes(fp);
	// value.integer = value.integer + 1;
	cptxt.integer = rnd(value.integer, 0xabcdef0987654321);
	write_16_bytes(fpw,cptxt);
	dectxt.integer = dec_rnd(cptxt.integer, 0xabcdef0987654321);
	write_16_bytes(fpw2,dectxt);
	// value = read_16_bytes(fp);
	// value.integer = value.integer + 1;
	// write_16_bytes(fpw,value);
	return 0;
}
