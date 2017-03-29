#include<stdio.h>
#include<stdint.h>

union bits128
{
    __uint128_t integer;
    unsigned char byte[16];
};

// Read part is cupping for some reason
__uint128_t read_16_bytes(FILE *fp)
{
	__uint128_t ret_val = 0;
	char buffer;
	int i;
	for(i=0;i<16;i++)
	{
		fread(&buffer, 1, 1, fp);
		printf("Buffer value: %d\n",(int)buffer);
		ret_val = (ret_val*8) + buffer;
	}
	union bits128 print;
	print.integer = ret_val;
	printf("IN read\n");
	for(i=15;i>=0;i--)
	{
		//fprintf(fpw,"%c",(int)print.byte[i]);
		printf("%d ",(int)print.byte[i]);
	}
	printf("\n");
	return ret_val;
}

void write_16_bytes(FILE *fpw,__uint128_t value)
{
	/* // This code has some error.
	__uint128_t temp;
	int i,byte;
	temp = value;
	for(i=0;i<16;i++)
	{
		byte = (int)value%256;
		printf("%d ",(256+(int)byte)%256);
		value = value/256;
	}
	printf("\n");*/
	union bits128 print;
	print.integer = value;
	int i;
	// This step depends on the endianness of the system.
	for(i=15;i>=0;i--)
	{
		fprintf(fpw,"%c",(int)print.byte[i]);
		printf("%d ",(int)print.byte[i]);
	}
	printf("\n");
}

// For testing
int main()
{
	FILE *fp,*fpw;
	fp = fopen("../File Generator/5.txt","rb");
	fpw = fopen("../File Generator/5_write.txt","wb");
	char buffer;
	__uint128_t value;
	value = read_16_bytes(fp);
	write_16_bytes(fpw,value);
	value = read_16_bytes(fp);
	write_16_bytes(fpw,value);
	return 0;
}
