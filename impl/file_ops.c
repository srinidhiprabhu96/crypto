#include<stdio.h>
#include<stdint.h>
<<<<<<< HEAD
#include "common_new.c"
=======
#include "common.c"
#include<time.h>
#include<math.h>
// The space of this union is also 128 bits.
union bits128
{
    __uint128_t integer;
    unsigned char byte[16];
};
>>>>>>> a25167c4fd913df447d40ef98553c50777da07c8

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
	// union bits128 value, cptxt, dectxt, key;
	// value = read_16_bytes(fp);
	// key.integer = 0xabcdef0987654321;
	// // value.integer = value.integer + 1;
	// cptxt = rnd(value, key);
	// write_16_bytes(fpw,cptxt);
	// dectxt = dec_rnd(cptxt, key);
	// write_16_bytes(fpw2,dectxt);
	// // value = read_16_bytes(fp);
	// // value.integer = value.integer + 1;
	// // write_16_bytes(fpw,value);
	char file_pt[100],file_ct[100],file_dt[100];
	union bits128 value, cptxt, dectxt;
	int i;
	for(i=5;i<=20;i++)
	{
		sprintf(file_pt,"../File Generator/%d.txt",i);
		sprintf(file_ct,"%d_ct.txt",i);
		sprintf(file_dt,"%d_dt.txt",i);
		fp = fopen(file_pt,"rb");
		fpw = fopen(file_ct,"wb");
		fpw2 = fopen(file_dt,"wb");
		int size,j;
		fseek(fp, 0L, SEEK_END);
		size = ftell(fp);
		rewind(fp);
		clock_t time = 0,start,end;
		for(j=0;j<size/16;j++)
		{
			value = read_16_bytes(fp);
			start = clock();
			cptxt.integer = encrypt(value.integer, 0xabcdef0987654321);
			end = clock();
			time += (end - start);
			/*write_16_bytes(fpw,cptxt);
			dectxt.integer = decrypt(cptxt.integer, 0xabcdef0987654321);
			write_16_bytes(fpw2,dectxt);*/
		}
		printf("File size: %lf\n",pow(2,i));
		printf("Total encrypt time: %lf\n",(double)(time)/CLOCKS_PER_SEC);
	}
	return 0;
}
