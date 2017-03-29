#include<stdio.h>
#include<stdint.h>

// The space of this union is also 128 bits.
union bits128
{
    __uint128_t integer;
    unsigned char byte[16];
};

// Read part is cupping for some reason
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
	FILE *fp,*fpw;
	fp = fopen("../File Generator/5.txt","rb");
	fpw = fopen("../File Generator/5_write.txt","wb");
	char buffer;
	union bits128 value;
	value = read_16_bytes(fp);
	value.integer = value.integer + 1;
	write_16_bytes(fpw,value);
	value = read_16_bytes(fp);
	value.integer = value.integer + 1;
	write_16_bytes(fpw,value);
	return 0;
}
